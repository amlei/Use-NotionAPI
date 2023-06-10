# With-NotionAPI
> Saving data of the books and videos data to notion page with Python . 

>使用Python将图书和影视数据存放入Notion中。

# 🗣️Language  

[English](./README.md)

[中文简体](./README%20-%20Chinese%20Simplified)

# 🖼️Environment

- Python 3.9+
- PyCharm 2021+

# 🎈Attention

The progarmming is during test phase, so I not sure it can greate running in your mechaine. Furthermore, I am also trying build better function. If you have discover some problems in the programming and that be willing told to me, while I am very will to solving its. Think you!

# 🤖Action

## 1. Ready

Have two account, them are both "[Douban](https://www.douban.com/)" and [Notion](https://www.notion.so/).

## 2. Modify Necessarily Data

A begin with, modify some necessarily data that are website and Notion API. For webiste, it is "[Douban](https://www.douban.com/)"(A platform of remark books and films) both  URL and Cookie. For [Notion API](https://developers.notion.com/), it is both token and id of database or pages.



In addition, modify other default information about book, which are star, status, bookCategory, bookRemark and bookExcerpt. 

## 3. About Code Files

- Package
  - data
    - user.py
    - book.py
  - deal
    - bookInfo.py
    - spider.py
  - pythons
    - base.py

- main.py

![image-20230409200159814](assets/image-20230409200159814.png)



Accoding to the user.py can know it save data and function.

book.py for other python files to quote data.

bookInfo.py during testing (Addition export cover link into file is csv on April 9,2023).

spider.py is main function of  spider website.

At present saving data and running main file in main.py.

In pythons packages under file is both Stack and Queue. 

## 4. Running

You must go throught  [Second Step](#2. Modify Necessarily Data)  can complete running main.py.

# 🎗️For Example

![image-20230331205442903](assets/image-20230331205442903.png)

![image-20230331205436292](assets/image-20230331205436292.png)

[With Notion API——Contain data of the books and videos in Douban website and that update into Notion database_bilibili](https://www.bilibili.com/video/BV15o4y1W7hw/?spm_id_from=333.999.0.0)

# 🔗Other Link

[Create Notion API](https://www.notion.so/my-integrations)
