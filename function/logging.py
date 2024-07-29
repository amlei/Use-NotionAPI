# -*- coding: UTF-8 -*-
"""
@Project: Use-API
@File: logging.py
@Date ：2024/7/17 11:04
@Author：Amlei (lixiang.altr@qq.com)
@version：python 3.12
@IDE: PyCharm 2023.2
@Description:
"""
import sys
from datetime import datetime
from loguru import logger


class Logging:
    def __init__(self):
        logger.add(f"./log/{datetime.now().strftime('%Y-%m-%d')}.log")

    def debug(self, content) -> None:
        logger.debug(content)

    def info(self, content) -> None:
        logger.info(content)

    def warning(self, content) -> None:
        logger.warning(content)

    def error(self, content) -> None:
        logger.error(content)


if __name__ == '__main__':
    Logging().debug("test")
