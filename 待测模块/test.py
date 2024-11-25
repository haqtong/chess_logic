# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='short_term.log', level=logging.INFO, format=LOG_FORMAT)


original_list = [4,3,2,1]

# 创建一个包含元素及其原始索引的元组列表
indexed_list = list(enumerate(original_list))

# 对新列表进行排序，排序依据是元素值
sorted_indexed_list = sorted(indexed_list, key=lambda x: x[1])
print(sorted_indexed_list)
