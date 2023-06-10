# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: spider_duban.py
@Date: 2023/3/27 14:26
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
import re
import requests
from data import web
from data import gol
from bs4 import BeautifulSoup
from pythons.base import Stack

class Book(gol.Option):
    def __init__(self, page: int = None):
        super().__init__()
        """
        默认为书籍，不修改self.option
        无论怎样继承该类调用get方法都不会最终影响全局的option
        所以在调用的子类中需要再次使用get方法，尽管不是重写
        """
        self.url = web.URL(Class=self.option, page=page).url
        self.header = web.URL(self.option).Header

        """
        初始化栈
        """
        self.Title = Stack()
        self.Author = Stack()
        self.Tag = Stack()
        self.Date = Stack()
        self.Comment = Stack()
        self.CoverLink = Stack()
        self.Star = Stack()

    def get(self):
        # Send a GET request to the URL and parse the HTML content using BeautifulSoup
        response = requests.get(self.url, headers=self.header)

        return BeautifulSoup(response.content, "html.parser")

    def title(self):
        # Find all the a tags with a "title" attribute and print their text content
        count = 0
        a_tage = self.get().find_all('a', {'title': True})

        for a in a_tage:
            self.Title.push(a['title'])
            # print(a['title'])
            count += 1
            if gol.MAXPage().page <= count:
                break

        return self.Title

    def author(self):
        pattern = r"\[[^\]]*\]||（[.*]）"
        # Find all the div tags with class "pub" and replace any "/" characters with a space
        for div in self.get().find_all("div", {"class": "pub"}):
            # Replace any "/" characters in the text content of the div tag with a space
            text = div.text.strip().replace(" ", "").split("/")
            # Remove any square brackets and their contents from the text content
            Author_text = re.sub(pattern, "", text[0])

            self.Author.push([Author_text, text[1:-1]])  # 存放入栈
        return self.Author

    def tags(self):
        for div in self.get().find_all("span", {"class": "tags"}):
            print(div.text.split(" ")[1:])
            self.Tag.push(div.text.split(" ")[1:])
        return self.Tag

    def date(self):
        for div in self.get().find_all("span", {"class": "date"}):
            print(div.text.replace("\n      读过", ""))
            self.Date.push(div.text.replace("\n      读过", ""))
        return self.Date

    def comment(self):
        for div in self.get().find_all("p", {"class": "comment"}):
            print(div.text.strip())
            self.Comment.push(div.text.strip())
        return self.Comment

    def coverLink(self):
        for div in self.get().find_all("img", {"width": "90"}):
            self.CoverLink.push(div.get("src"))
        return self.CoverLink

    # 评分
    def rating(self):
        # 使用正则表达式匹配class包含rating和数字的span标签
        pattern = re.compile(r'rating\d+-t')
        span_tags = self.get().find_all('span', {'class': pattern})

        # 取每个span标签的数字部分
        for span_tag in span_tags:
            rating_class = span_tag.get('class')
            rating = re.search(r'\d+', str(rating_class)).group()
            self.Star.push(rating)
        return self.Star

class Video(Book, gol.Option):
    def __init__(self, page: int = None):
        super().__init__()
        self.option = 1
        self.url = web.URL(Class=self.option, page=page).url

    def get(self):
        # Send a GET request to the URL and parse the HTML content using BeautifulSoup
        response = requests.get(self.url, headers=self.header)
        return BeautifulSoup(response.content, "html.parser")

    def title(self):
        em_tags = self.get().find_all('em')

        for em in em_tags:
            self.Title.push(em.text.split("/")[0].strip(" "))
        return self.Title

    def other(self):
        # 观看日记
        span_date_tags = self.get().find_all('span', {'class': 'date'})
        # 标签
        span_tags = self.get().find_all('span', {'class': 'tags'})
        # 短评
        span_comment_tags = self.get().find_all('span', {'class': 'comment'})

        for span in span_date_tags:
            self.Date.push(span.text)

        for span in span_tags:
            self.Tag.push(span.text.strip("标签: ").split(" "))

        for span in span_comment_tags:
            self.Comment.push(span.text)

        # 返回顺序为：self.Date: 0, self.Tag: 1, self.Comment: 2
        return self.Date, self.Tag, self.Comment

    def coverLink(self):
        # 查找所有包含title属性的a标签
        a_tags = self.get().find_all('a', title=True)

        # 查找每个a标签内包含的img标签
        for a_tag in a_tags:
            img_tag = a_tag.find('img')
            if img_tag:
                self.CoverLink.push(img_tag.get('src'))

        return self.CoverLink

if __name__ == '__main__':
    c = Book(page=15).coverLink()
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.pop())

    print("Video")
    c = Video(page=15).coverLink()
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.pop())
    print(c.pop())
