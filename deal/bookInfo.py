# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: bookInfo.py
@Date: 2023/3/30 20:31
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
from data.book import book
from data.user import data
import pandas

"""
本文件调试中
"""
class info():
    def __init__(self):
        self.list = []
        self.book = book()
        self.user = data()

    def renew(self):
        self.list = []

    # 作者
    def author(self):
        for i in range(self.user.maximum):
            AuthorContent = self.book.author.pop()
            authorPerson = AuthorContent[0].split("、")  # 作者
            print(authorPerson)
            for j in range(len(authorPerson)):
                self.list.append(dict(name=authorPerson[j]))
        return self.list

    def coverLink(self):
        text = []
        for i in range(self.user.maximum):
            text.append([self.book.BookTitle.pop(), str(self.book.link.pop())])

        content = pandas.DataFrame(text, columns=["Book", "Cover"])
        del text
        content.to_csv("./data/book.csv", encoding="GBK", index=True)

if __name__ == '__main__':
    # 如果是在本文件下运行，需要将"./data"的引用更改为: "../data"
    info().coverLink()

    # print(info().author())
    # print(type(info().author()))
    # print(type(info().author()[0]))


