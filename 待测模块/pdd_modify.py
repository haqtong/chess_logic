# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='short_term.log', level=logging.INFO, format=LOG_FORMAT)

from config.set_config import *
from 待测模块.pdd_creator import *
def exec():
    infn = os.path.join(Config_base.data_warehouse,'chess_val.json')
    chess_val = Config_base.read_data(infn)
    lst_1 = chess_val['一费卡']
    lst_2 = chess_val['二费卡']
    lst_3 = chess_val['三费卡']
    lst_4 = chess_val['四费卡']
    lst_5 = chess_val['五费卡']
    lst_01 = lst_1+lst_2
    # print(lst_01)
    lst_02 = lst_3
    pdd_ = pdd()
    pdd_.jbscq(lst_01,lst_02,[6,1,7])



if __name__ == '__main__':
    exec()