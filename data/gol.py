# -*- coding: UTF-8 -*-
"""
@Project: Project
@File: gol.py
@Date: 2023/6/10 14:18
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""

# 继承异常类，自定义输出异常
class Error(Exception):
    def __repr__(self):
        pass

class MAXPage():
    def __init__(self):
        self.page = 15

# 书籍或影片
class Option:
    def __init__(self):
        """
        self.option: 0:Book 1:Video
        """
        self.option = 0

    def get(self):
        return self.option

if __name__ == '__main__':
    class vi(Option):
        def __init__(self):
            super().__init__()
            self.option = 1

        def __repr__(self):
            string = "获取的是"
            if self.option == 0:
                print(f"{string}书籍")
            if self.option == 1:
                print(f"{string}影视")
            else:
                raise Error("列表获取错误！请在0与1之间选择，0：书籍  1：影视。")
