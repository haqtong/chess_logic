# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
from config.set_config import *
from 待测模块.pdd_creator import *

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='short_term.log', level=logging.INFO, format=LOG_FORMAT)


def exec():
    _ = chess()
    _.ylzdyw()

if __name__ == '__main__':
    exec()