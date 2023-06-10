# -*- coding: UTF-8 -*-
"""
@Project: Project
@File: Update.py
@Date: 2023/6/10 13:22
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""

from data import gol

class URL:
    def __init__(self, Class: int, page: int = 0):
        """
        Class: 0:book 1:movie
        page: 决定页数，默认情况下只查找一页，若需要多页只需加上对应次数的15即可,也就是self.page加它自己: gol.MAXPage()
        """
        self.Content = gol.Option().getString()

        self.url = f"https://{self.Content[Class]}" \
                   f".douban.com/people/{'你的豆瓣号'}/collect?" \
                   f"start={page}&sort=time&rating=all&filter=all&mode=grid"
        self.Header = {
            "Cookie": '',
            "Accept": '',
            "User-Agent": ''
        }
