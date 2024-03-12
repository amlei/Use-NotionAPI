# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: main.py
@Date: 2023/3/27 11:55
@Author: YaPotato
@version: python 3.12
@IDE: PyCharm 2023.1
"""
import os
from datetime import datetime
from time import sleep
from typing import Any, Dict, List

from dotenv import load_dotenv
from notion_client import Client
from function.glo import Glo
from function.spider import Book, Video


class Run:
    def __init__(self, option: int = 0, page: int = 0):
        """
        :param option: 类型选择，书籍、影视剧
        :param page: 以 15 为步长增加
        """
        load_dotenv()
        self.client = Client(auth=Glo.Token['Book'])
        self.page: int = page
        self.title: str = ""
        self.count: int = 0

        match option:
            case Glo.book:
                self.classify = Book(page=page)
                self.classify.title()
                self.classify.author()
                self.classify.tags()
                self.classify.date()
                self.classify.comment()
                self.classify.cover_link()
                self.classify.rating()
                self.valid: bool = self.classify.valid
                self.valid_num: int = self.classify.valid_num
            case _:
                self.classify = Video()

    def lasted_book(self):
        with open("./lasted_mark.txt", "w", encoding="utf-8") as f:
            f.writelines(self.title)

    def create_page(self) -> int:
        """
        创建页面
        :return: 返回页面 ID
        """
        self.title: str = self.classify.Titles.pop(0)
        # 当前更新阅读的最后一本书则放入探测文件
        if self.page == 0:
            self.lasted_book()

        new_page: dict = {
            "title": [
                {
                    "text": {
                        "content": f"《{self.title}》"
                    }
                }
            ]
        }
        created_page = self.client.pages.create(parent={"database_id": Glo.DatabaseID['Book']}, properties=new_page)
        # 存储创建的页面 ID
        pageID = created_page['id']
        print(f"《{self.title}》创建成功!")
        self.count += 1
        return pageID

    def print_all(self) -> None:
        """
        输出全部数据
        :return:
        """
        print(self.classify.Titles)
        print(self.classify.Authors)
        print(self.classify.Comments)
        print(self.classify.CoverLinks)
        print(self.classify.Ratings)
        print(self.classify.Tags)
        print(self.classify.Dates)
        print()

    def progress(self) -> dict:
        """
        参数处理
        :return: 返回页面参数
        """
        # 根据数据长度更新书籍类别
        category: list = []
        # 作者，同上原理
        author: list = []
        date: str = ""
        AuthorContent: list = self.classify.Authors.pop(0)


        match len(AuthorContent[1]):
            # ["化学工业出版社，[]]
            case 0:
                publishingCompany = AuthorContent[0]
            # 存在译者情况['弗朗西斯·苏（FrancisSu）', ['沈吉儿、韩潇潇', '中信出版集团', '2022-6-10', '69']]
            case 3:
                publishingCompany = AuthorContent[1][1]
            # 默认情况
            case _:
                publishingCompany = AuthorContent[1][0]
        try:
            publishingDate = AuthorContent[1][-1].split("-")
            # 忽略日期，且月份必须有两位数（剩下一位由0填充）
            date = "{}-{:0>2}-01".format(publishingDate[0], publishingDate[1])
        except IndexError:
            # 获取日期超过范围，说明该书没有出版日期信息
            today = datetime.now().strftime("%Y-%m-%d")
            print(f"捕获到{AuthorContent[0]}书籍出现出版日期错误，日期填充已更改为今日({today})请完成数据填充后自行更改")
            date = today

        # 作者
        for j in AuthorContent[0].split("、"):
            author.append(dict(name=j))

        # 书籍分类
        tags = self.classify.Tags.pop(0)
        for j in range(len(tags)):
            category.append(dict(name=tags[j]))

        properties = {
            "状态": {
                "select": {
                    "name": os.environ.get("STATUS").split("|")[0]
                }
            },
            "评分": {
                "select": {
                    "name": self.classify.Ratings.pop(0)
                }
            },
            "来源": {
                "select": {
                    "name": os.environ.get("CATEGORY")
                }
            },
            "短评": {
                "rich_text": [
                    {
                        "text": {
                            "content": self.classify.Comments.pop(0)
                        }
                    }
                ]
            },
            "读完时间": {
                "date": {
                    "start": self.classify.Dates.pop(0)
                }
            },
            "出版社": {
                "select": {
                    "name": str(publishingCompany)
                }
            },
            "出版日期": {
                "date": {
                    "start": date
                }
            },
            "作者": {
                "multi_select": author

            },
            "类别": {
                "multi_select": category
            },
            "书评": {
                "select": {
                    "name": os.environ.get("COMMENT")
                }
            },
            "书摘": {
                "select": {
                    "name": os.environ.get("MARK")
                }
            }
        }

        return properties

    def update(self):
        # 图标
        icon: dict = {
            "type": "external",
            "external": {
                "url": "https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f4d8.svg"
            }
        }

        for i in range(Glo.MAXNum):
            property: dict = self.progress()
            # 背景图
            cover = {
                "type": "external",
                "external": {
                    "url": self.classify.CoverLinks.pop(0)
                }
            }
            sleep(2)
            self.client.pages.update(page_id=self.create_page(), properties=property, icon=icon, cover=cover)


if __name__ == '__main__':
    page: int = 0
    while True:
        run = Run(page=page)
        run.print_all()
        run.update()
        page += 15
        sleep(5)
        if run.valid is False and run.count == run.valid_num:
            break

        print("下一页")
