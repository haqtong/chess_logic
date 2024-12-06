# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
from config.set_config import *
from 待测模块.pdd_creator import *

file_path = os.path.join(Config_base.data_warehouse, 'ylzdyw.json')
result = Config_base.read_data(file_path)
new_result = {k: v for k, v in result.items() if len(v)>0}
index = list(new_result.keys())
reword = list(new_result.values())

aim_df = pd.DataFrame([index,reword]).T
aim_df.columns = ['点数','奖励']
outfn = 'result.xlsx'

Config_base.dumps_data(aim_df,outfn)


