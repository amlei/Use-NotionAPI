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
from dotenv import load_dotenv
from notion_client import Client
from function.glo import Glo
from function.spider import Book, Video


class Run:
    def __init__(self, option: int = 0):
        load_dotenv()
        self.token = Client(auth=Glo.Token['Book'])
        match option:
            case Glo.book:
                self.classify = Book()
                self.classify.title()
                self.classify.author()
                self.classify.tags()
                self.classify.date()
                self.classify.comment()
                self.classify.cover_link()
                self.classify.rating()
            case _:
                self.classify = Video()

    def create_page(self) -> int:
        """
        创建页面
        :return: 返回页面 ID
        """
        title = self.classify.Titles.pop(0)
        new_page: dict = {
            "title": [
                {
                    "text": {
                        "content": f"《{title}》"
                    }
                }
            ]
        }
        created_page = self.token.pages.create(parent={"database_id": Glo.DatabaseID['Book']}, properties=new_page)
        # 存储创建的页面 ID
        pageID = created_page['id']
        print(f"创建《{title}》成功!")
        return pageID

    def print_all(self):
        print(self.classify.Titles)
        print(self.classify.Authors)
        print(self.classify.Comments)
        print(self.classify.CoverLinks)
        print(self.classify.Ratings)
        print(self.classify.Tags)
        print(self.classify.Dates)

    def update(self):
        """
        更新页面信息栏
        :return:
        """
        for i in range(Glo.MAXNum):
            # 根据数据长度更新书籍类别
            categoryBook = []
            # 作者，同上原理
            author = []
            AuthorContent = self.classify.Authors.pop(0)

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
                formatDate = "{}-{:0>2}-01".format(publishingDate[0], publishingDate[1])
            except IndexError:
                # 获取日期超过范围，说明该书没有出版日期信息
                today = datetime.now().strftime("%Y-%m-%d")
                print(f"捕获到{AuthorContent[0]}书籍出现出版日期错误，日期填充已更改为今日({today})请完成数据填充后自行更改")
                formatDate = today

            # 作者
            authorPerson = AuthorContent[0].split("、")  # 作者
            for j in range(len(authorPerson)):
                author.append(dict(name=authorPerson[j]))

            # 书籍分类
            tags = self.classify.Tags.pop(0)
            for j in range(len(tags)):
                categoryBook.append(dict(name=tags[j]))

            properties_to_update = {
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
                        "start": formatDate
                    }
                },
                "作者": {
                    "multi_select": author

                },
                "类别": {
                    "multi_select": categoryBook
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
                },
                "icon": {
                    "type": "emoji",
                    "emoji": "https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f4d8.svg"
                },
                # "cover": {
                #     "type": "external",
                #     "external": {
                #         "url": self.classify.CoverLinks.pop(0)
                #     }
                # }
            }

            # Update the page properties
            self.token.pages.update(page_id=self.create_page(), properties=properties_to_update)


if __name__ == '__main__':
    run = Run()
    run.print_all()
    run.update()