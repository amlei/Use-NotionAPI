# -*- coding: UTF-8 -*-
"""
@Project: Use-API
@File: spider.py
@Date ：2024/3/12 14:43
@Author：Amlei (lixiang.altr@qq.com)
@version：python 3.12
@IDE: PyCharm 2023.2
"""
import re
import requests
from typing import Any, Tuple, List
from bs4 import BeautifulSoup
from function.glo import douban
from function.glo import Glo


class Book:
    def __init__(self, page: int = 0):
        self.url: str = douban(Glo.book, page)
        self.header: dict[str] = Glo.header
        self.MaxBook: int = Glo.MAXNum
        self.request: BeautifulSoup = self.get()
        self.valid_num: int = 0
        self.valid: bool = True
        self.lasted_book: str = ""

        self.Titles: list[str | Any] = []
        self.Authors: list[str | Any] = []
        self.Tags: list[str | Any] = []
        self.Dates: list[str | Any] = []
        self.Comments: list[str | Any] = []
        self.CoverLinks: list[str | Any] = []
        self.Ratings: list[str | Any] = []

    def refresh(self) -> None:
        """
        清空栈堆
        :return: None
        """
        self.Titles: list[str | Any] = []
        self.Authors: list[str | Any] = []
        self.Tags: list[str | Any] = []
        self.Dates: list[str | Any] = []
        self.Comments: list[str | Any] = []
        self.CoverLinks: list[str | Any] = []
        self.Ratings: list[str | Any] = []

    def get(self) -> BeautifulSoup:
        response = requests.get(self.url, headers=self.header)
        self.request: BeautifulSoup = BeautifulSoup(response.text, "html.parser")

        return self.request

    def title(self) -> list[str]:
        """
        以书名探测新增阅读数量
        :return: 书名
        """
        # Find all the a tags with a "title" attribute and print their text content
        count: int = 0
        file = open("./last_mark.txt", "r", encoding="utf-8")
        last_book = file.readlines().pop()
        file.close()

        for i in self.request.find_all("a", {"title": True}):
            for span in i.find_all("span"):
                span.extract()
            self.Titles.append(i.text.strip())

            # 仅获取图书数目标题
            count += 1
            self.valid_num += 1
            if count == self.MaxBook or i.text.strip() == last_book:
                self.valid = False
                break

        return self.Titles

    def author(self):
        pattern = r"\[[^\]]*\]||（[.*]）"
        for div in self.request.find_all("div", {"class": "pub"}):
            text = div.text.strip().replace(" ", "").split("/")

            self.Authors.append([re.sub(pattern, "", text[0]), text[1:-1]])

        return self.Authors

    def tags(self) -> list[str]:
        for div in self.request.find_all("span", {"class": "tags"}):
            self.Tags.append(div.text.split(" ")[1:])

        return self.Tags

    def date(self) -> list[str]:
        for div in self.request.find_all("span", {"class": "date"}):
            self.Dates.append(div.text.replace("\n      读过", ""))

        return self.Dates

    def comment(self) -> list[str]:
        for div in self.request.find_all("p", {"class": "comment"}):
            self.Comments.append(div.text.strip())

        return self.Comments

    def cover_link(self) -> list[str]:
        for div in self.request.find_all("img", {"width": "90"}):
            self.CoverLinks.append(div.get("src"))

        return self.CoverLinks

    def rating(self) -> list[str]:
        # 使用正则表达式匹配class包含rating和数字的span标签
        pattern = re.compile(r'rating\d+-t')
        span_tags = self.get().find_all('span', {'class': pattern})

        # 取每个span标签的数字部分
        for span_tag in span_tags:
            rating_class = span_tag.get('class')
            rating = re.search(r'\d+', str(rating_class)).group()
            self.Ratings.append(rating)

        new_stack: list[str] = []
        for i in range(Glo.MAXNum):
            s = int(self.Ratings.pop())
            new_stack.append(Glo.star[:(s * 2)])
        new_stack.reverse()
        self.Ratings = new_stack

        return new_stack


class Video(Book):
    def __init__(self, page: int = None):
        super().__init__()
        self.url: str = douban(Glo.movie, page)
        self.request: BeautifulSoup = self.get()
        self.refresh()

    def get(self) -> BeautifulSoup:
        response = requests.get(self.url, headers=self.header)

        return BeautifulSoup(response.content, "html.parser")

    def title(self) -> list[str]:
        em_tags = self.get().find_all('em')

        for em in em_tags:
            self.Titles.append(em.text.split("/")[0].strip(" "))
        return self.Titles

    def other(self) -> tuple[list[str | Any], list[str | Any], list[str | Any]]:
        # 观看日记
        span_date_tags = self.get().find_all('span', {'class': 'date'})
        # 标签
        span_tags = self.get().find_all('span', {'class': 'tags'})
        # 短评
        span_comment_tags = self.get().find_all('span', {'class': 'comment'})

        for span in span_date_tags:
            self.Dates.append(span.text)

        for span in span_tags:
            self.Tags.append(span.text.strip("标签: ").split(" "))

        for span in span_comment_tags:
            self.Comments.append(span.text)

        # 返回顺序为：self.Date: 0, self.Tag: 1, self.Comment: 2
        return self.Dates, self.Tags, self.Comments

    def cover_link(self) -> list[str]:
        # 查找所有包含title属性的a标签
        a_tags = self.get().find_all('a', title=True)

        # 查找每个a标签内包含的img标签
        for a_tag in a_tags:
            img_tag = a_tag.find('img')
            if img_tag:
                self.CoverLinks.append(img_tag.get('src'))

        return self.CoverLinks

if __name__ == '__main__':
    # book = Book()
    # book.title()
    # book.author()
    # book.comment()
    # book.cover_link()
    # book.rating()
    # book.tags()
    # book.date()

    # print(book.Titles)
    # print(book.author())
    # print(book.comment())
    # print(book.cover_link())
    # print(book.rating())
    # print(book.tags())
    # print(book.date())

    read_file = open("../last_mark.txt", "r", encoding="utf-8")
    book = read_file.readlines()
    read_file.close()
    while True:
        print(book)