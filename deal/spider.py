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
from data import user
from bs4 import BeautifulSoup
from pythons.base import Stack

data = user.data()
class deal():
    def __init__(self):
        self.stack = Stack()        # 引入栈
        self.url = data.url
        self.header = data.cookie
        self.MaxBook = data.maximum
        self.get = self.get()

    def renew(self):                # 清空堆栈
        self.stack = Stack()

    def get(self):
        # Send a GET request to the URL and parse the HTML content using BeautifulSoup
        response = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup

    def bookTitle(self):
        # Find all the a tags with a "title" attribute and print their text content
        count = 0
        for a in self.get.find_all("a", {"title": True}):
            for span in a.find_all("span"):
                span.extract()
            text = a.text.strip()
            self.stack.push(text)
            count += 1
            if count == self.MaxBook:
                break

        return self.stack

    def author(self):
        pattern = r"\[[^\]]*\]||（[.*]）"
        # Find all the div tags with class "pub" and replace any "/" characters with a space
        for div in self.get.find_all("div", {"class": "pub"}):
            # Replace any "/" characters in the text content of the div tag with a space
            text = div.text.strip().replace(" ", "").split("/")
            # Remove any square brackets and their contents from the text content
            Author_text = re.sub(pattern, "", text[0])
            # Print the cleaned text content
            # Author.push([Author_text, text[1:-1]])  # 存放入栈
            self.stack.push([Author_text, text[1:-1]])  # 存放入栈

        return self.stack

    def tags(self):
        for div in self.get.find_all("span", {"class": "tags"}):
            self.stack.push(div.text.split(" ")[1:])
        return self.stack

    def Date(self):
        for div in self.get.find_all("span", {"class": "date"}):
            self.stack.push(div.text.replace("\n      读过", ""))
        return self.stack

    def comment(self):
        for div in self.get.find_all("p", {"class": "comment"}):
            self.stack.push(div.text.strip())
        return self.stack

    def coverLink(self):
        for div in self.get.find_all("img", {"width": "90"}):
            self.stack.push(div.get("src"))
        return self.stack


if __name__ == '__main__':
    deal().coverLink()
