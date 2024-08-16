# -*- coding: UTF-8 -*-
"""
@Project: Use-API
@File: glo.py
@Date ：2024/3/12 14:42
@Author：Amlei (lixiang.altr@qq.com)
@version：python 3.12
@IDE: PyCharm 2023.2
"""
import os
from dotenv import load_dotenv
from loguru import logger
load_dotenv()


class Glo:
    """
    全局数据
    """
    # 单页最大数量
    MAXNum: int = 15
    option_classify: int = os.environ.get("CLASSIFY")
    book: int = 0
    video: int = 1

    # Notion 数据: Token、Database ID
    Token = os.environ.get("TOKEN")

    Book_Databases_ID = os.environ.get("BOOK_DATABASE_ID")
    Video_Databases_ID = os.environ.get("VIDEO_DATABASE_ID")

    # 个人头文件
    header: dict[str] = {
        "Cookie": os.environ.get("COOKIE"),
        "Accept": os.environ.get("ACCEPT"),
        "User-Agent": os.environ.get("USER_AGENT")
    }

    # 数据信息
    star: str = os.environ.get("STAR")
    logger.info("Get data for global.")


def douban(select: int = 0, page: int = 0) -> str:
    """
    :param select: 选择数据类型
    :param page: 页面
    :return: 返回对应类型 URL
    """
    doubanID: str = os.environ.get("DOUBANID")
    classify: str = os.environ.get("CLASSIFY")
    match select:
        case 0:
            classify = "book"
        case 1:
            classify = "movie"

    url: str = f"https://{classify}.douban.com/people/{doubanID}/collect?start={page}&sort=time&rating=all&filter=all&mode=grid"

    return url