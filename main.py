# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: NotionPage.py
@Date: 2023/3/27 11:55
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
from notion_client import Client
from datetime import datetime
from pythons.base import Queue
from data.user import data
from data.book import book
from deal.bookInfo import info

"""
···························································分割线························································
"""
userdata = data()
bookData = book()
# Initialize client object
token = Client(auth=userdata.Token)
# Define the database ID and create a new page object
database_id = userdata.databaseID
queue = Queue()
info().coverLink()

# 并不需要休眠，否则等待时间非常长
"""创建新页面"""
try:
    while (bookData.BookTitle.size() > 0):
        new_page = {
            "title": [
                {
                    "text": {
                        "content": f"《{bookData.BookTitle.peek()}》"
                    }
                }
            ]
        }

        # Add the new page to the database
        created_page = token.pages.create(parent={
            "database_id": database_id
        }, properties=new_page)

        queue.enqueue(created_page['id'])     # 存储新页面的ID
        print(f"《{bookData.BookTitle.peek()}》 Succeed!")
        bookData.BookTitle.pop()     # 释放空间
except Exception as e:
    print(f"Error!\n{e}")
    pass

"""
Update data after create new page
"""
try:     # 极少书籍不包含评论或评星，跳过
    for i in range(userdata.maximum):
        # 根据数据长度更新书籍类别
        categoryBook = []
        # 作者，同上原理
        author = []
        AuthorContent = bookData.author.pop()


        try:
            if len(AuthorContent[1]) == 3:  # 存在译者情况  ['弗朗西斯·苏（FrancisSu）', ['沈吉儿、韩潇潇', '中信出版集团', '2022-6-10', '69']]
                publishingCompany = AuthorContent[1][1]
            elif len(AuthorContent[1]) == 0:    # ["化学工业出版社，[]]
                publishingCompany = AuthorContent[0]
            else:   # ['李开复"，['浙江人民出版社 ，"2018-9-1']]
                publishingCompany = AuthorContent[1][0]

            try:
                publishingDate = AuthorContent[1][-1].split("-")
                formatDate = "{}-{:0>2}-01".format(publishingDate[0], publishingDate[1])   # 忽略日期，且月份必须有两位数（剩下一位由0填充）
            except IndexError:  # 获取日期超过范围，说明该书没有出版日期信息
                today = datetime.now().strftime("%Y-%m-%d")
                print(f"捕获到{AuthorContent[0]}书籍出现出版日期错误，日期填充已更改为今日({today})请完成数据填充后自行更改")
                formatDate = today

            # 作者
            authorPerson = AuthorContent[0].split("、")  # 作者
            for j in range(len(authorPerson)):
                author.append(dict(name=authorPerson[j]))

            # 书籍分类
            bookTags = bookData.tags.pop()
            for j in range(len(bookTags)):
                categoryBook.append(dict(name=bookTags[j]))

            properties_to_update = {
                "状态": {
                    "select": {
                        "name": userdata.status     # 默认：已读
                    }
                },
                "评分": {
                    "select": {
                        "name": userdata.star    # 默认: 5星
                    }
                },
                "来源": {
                    "select": {
                        "name": userdata.bookCategory       # 默认: 纸质书
                    }
                },
                "短评": {
                    "rich_text": [
                        {
                            "text": {
                                "content": bookData.comment.pop()
                            }
                        }
                    ]
                },
                "读完时间": {
                    "date": {
                        "start": bookData.Date.pop()
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
                        "name": userdata.bookRemark
                    }
                },
                "书摘": {
                    "select": {
                        "name": userdata.bookExcerpt
                    }
                }
            }

            # Update the page properties
            token.pages.update(page_id=queue.dequeue(),
                                properties=properties_to_update)

        except:
            pass
except Exception as e:
    print(e)
    pass

