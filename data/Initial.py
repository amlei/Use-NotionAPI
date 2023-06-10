# -*- coding: UTF-8 -*-
"""
@Project: Project
@File: Initial.py
@Date: 2023/6/10 11:27
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
# 初始化数据
class Initial:
    def __init__(self):
        # Token 码
        self.Token = {
            "Book": "secret_9yAkBCPLd5rakqZgiTqxdtGCqJTCoPQXGsA08yI8fLs",
            "Video": "secret_9yAkBCPLd5rakqZgiTqxdtGCqJTCoPQXGsA08yI8fLs"
        }

        # 数据库ID
        self.DatabaseID = {
            "Book": "c284686fbf50467898bf2c0cc224ba51",
            "Video": "ed8f1332c10b45698ce631598f39d5f0"
        }

        # 评分：默认5星,每颗星占两个字符
        self.star = "⭐️⭐️⭐️⭐️⭐️"
        self.Info = {
            "Book": {
                "Status": "读完",
                 "Comment": "不发布",
                 "Mark": "尚未整理",
                "Origin": None,
                "Author": None,
                "Class": None,
                "Publish": None,
                "Published": None,
                "Star": self.star
            }, "Video": {
                "Status": "已看",
                "Class": None,
                "Country": None,
                "Publish": None,
                "Watched": None,
                "Star": self.star
            }
        }

if __name__ == '__main__':
    # from notion_client import Client
    # init = Initial()
    # client = Client(auth=f"{init.Token['Book']}")
    # new_page = {
    #     "title": [
    #         {
    #             "text": {
    #                 "content": "《Test》"
    #             }
    #         }
    #     ]
    # }
    #
    # # Add the new page to the database
    # created_page = client.pages.create(parent={
    #     "database_id": f"{init.DatabaseID['Book']}"
    # }, properties=new_page)
    print(Initial().star)
    print(Initial().star[:8])
    print(Initial().star[:6])
    print(Initial().star[:4])
    print(Initial().star[:2])
