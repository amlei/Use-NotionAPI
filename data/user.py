# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: user.py
@Date: 2023/3/30 17:59
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
# from data.book import book

class data():
    def __init__(self):
        self.maximum = 15    # 一页最大书量

        self.url = "https://book.douban.com/mine?status=collect"
        self.cookie = {
            "User-Agent": "",
            "Cookie": ''
        }

        self.Token = ""
        self.databaseID = ""

        self.star = "⭐️⭐️⭐️⭐️⭐️"    # 默认: 5星
        self.status = "读完"          # 书籍状态，默认：读完
        self.bookCategory = "纸质书"   # 阅读类型，默认：纸质书
        self.bookRemark = "不发布"     # 书评，默认：不发布
        self.bookExcerpt = "尚未整理"       # 书摘，默认：尚未整理
