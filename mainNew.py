# -*- coding: UTF-8 -*-
"""
@Project: Python
@File: NotionPage.py
@Date: 2023/3/27 11:55
@Author: YaPotato
@version: python 3.11
@IDE: PyCharm 2023.1
"""
from data import Initial
from notion_client import Client
from datetime import datetime
from pythons.base import Queue

token = Client(auth=Initial.Initial().Token)
DatabaseID = Initial.Initial().DatabaseID

