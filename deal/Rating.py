# -*- coding: UTF-8 -*-
"""
@Project: Project
@File: Rating.py
@Date: 2023/6/10 18:27
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
import web
from data import gol, Initial
from pythons.base import Stack

class rating(Initial.Initial):
    def __init__(self):
        super().__init__()
        self.stack = Stack()

    def Star(self):
        data = web.Book().rating()
        for i in range(gol.MAXPage().page):
            s = int(data.pop())
            self.stack.push(self.star[:(s*2)])

        return self.stack

if __name__ == '__main__':
    c = rating().Star()
    for i in range(15):
        print(c.pop())


