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
图片保存, 默认情况保存书籍
"""
def coverLink():
    global title, link

    OpValue = gol.Option().getValue()
    # OpValue = 1
    text = []
    fileName = ""
    if OpValue == 0:
        fileName = "book"
        title = web.Book().title()
        link = web.Book().coverLink()
    elif OpValue == 1:
        fileName = "video"
        title = web.Video().title()
        link = web.Video().coverLink()

    for i in range(gol.MAXPage().get()):
        text.append([title.pop(), str(link.pop())])

    try:
        content = pandas.DataFrame(text, columns=["Title", "Cover"])
        content.to_csv(f"../result/{fileName}.csv", encoding="GBK", index=True)
    except PermissionError:
        raise gol.Error("File is Opening")

    del text

if __name__ == '__main__':
    coverLink()

