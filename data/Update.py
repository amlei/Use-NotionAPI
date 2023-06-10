# -*- coding: UTF-8 -*-
"""
@Project: Project
@File: Update.py
@Date: 2023/6/10 13:17
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
import pprint
from data import Initial as webInitial

web = webInitial.Initial

# 继承父类
class Update(web):
    # 更新数据信息
    def __init__(self):
        super().__init__()
        self.Info['Book']['Class'] = "123"

if __name__ == '__main__':
    var = Update().Info
    pprint.pprint(var)
