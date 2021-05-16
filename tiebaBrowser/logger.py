# -*- coding:utf-8 -*-
__all__ = ('SCRIPT_DIR',
           'MyLogger', 'log')


import os
import sys
from pathlib import Path
import time

import logging





class MyLogger(logging.Logger):
    """
    MyLogger(name=__name__)

    自定义的日志记录类
    """

    def __init__(self, name):

        super().__init__(name)
        self.setLevel(logging.DEBUG)


log = MyLogger(__name__)
