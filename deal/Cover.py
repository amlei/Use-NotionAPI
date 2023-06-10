# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: Cover.py
@Date: 2023/3/30 20:31
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
import pandas
from deal import web
from data import gol

"""
图片保存
"""

def coverLink():
    text = []
    title = web.Book().title()
    link = web.Book().coverLink()
    for i in range(gol.MAXPage().page):
        text.append([title.pop(), str(link.pop())])

    try:
        content = pandas.DataFrame(text, columns=["Book", "Cover"])
        content.to_csv("../data/book.csv", encoding="GBK", index=True)
    except PermissionError:
        raise gol.Error("File is Opening")

    del text

if __name__ == '__main__':
    coverLink()

