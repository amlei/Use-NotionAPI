# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: book.py
@Date: 2023/3/30 18:15
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
from deal.spider import deal
# from user import data

class book():
    def __init__(self):
        # 获取数据
        self.spider = deal()
        self.BookTitle = self.spider.bookTitle()                # 书名
        self.spider.renew()

        self.author = self.spider.author()    # 作者及其它内容
        self.spider.renew()

        self.tags = self.spider.tags()  # 类别标签
        self.spider.renew()

        self.Date = self.spider.Date()                             # 读完日期
        self.spider.renew()

        self.comment = self.spider.comment()                       # 评论
        self.spider.renew()

        self.link = self.spider.coverLink()
        self.spider.renew()

# if __name__ == '__main__':
    # for i in range(data().maximum):
    #     print(book().BookTitle.pop())
    #     print(book().author.pop())
    #     print(book().tags.pop())
    #     print(book().Date.pop())
    #     print(book().comment.pop())
    #     print(book().link.pop())
