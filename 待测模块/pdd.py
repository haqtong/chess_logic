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
import itertools
from collections import Counter

fn = 'chess_val.json'
fn_1 = 'chess_trait.json'
fn_2 = 'trait_chess_group_size.json'
chess_val_fn = os.path.join(Config_base.data_warehouse,fn)
chess_trait_fn = os.path.join(Config_base.data_warehouse,fn_1)
chess_group_size_fn  = os.path.join(Config_base.data_warehouse,fn_2)
chess_val = Config_base.read_data(chess_val_fn)
chess_trait = Config_base.read_data(chess_trait_fn)
chess_group_size = Config_base.read_data(chess_group_size_fn)


# 创建一个长度为30的列表（这里用数字0到29作为示例）

# 1-3费卡
lst_1 = chess_val['一费卡']
lst_2 = chess_val['二费卡']
lst_3 = chess_val['三费卡']
# lst_4 = chess_val['四费卡']
# lst_5 = chess_val['五费卡']
lst = lst_1+lst_2+lst_3
# extend_list =['德莱厄斯', '阿木木', '艾瑞莉娅', '薇古丝', '芮尔', '魔腾', '阿卡丽']
# lst.extend(extend_list)
# lst = lst_1+lst_2+lst_3+lst_4+lst_5

# lst.append('安蓓萨')
# 生成所有从lst中抽取7个元素的组合
all_combinations = list(itertools.combinations(lst, 7))# 26978328
trait_group = {}
group_size = []
for ind,group in enumerate(all_combinations):
    tmp_trait = []
    for chess in group:
        tmp_trait.extend(chess_trait[chess])

    trait_group[ind] = dict(Counter(tmp_trait))
    for key,val in dict(Counter(tmp_trait)).items():
        if val < chess_group_size[key][0]:
            trait_group[ind].pop(key)
    group_size.append(len(trait_group[ind].keys()))



# 创建一个包含元素及其原始索引的元组列表
indexed_list = list(enumerate(group_size))
# 对新列表进行排序，排序依据是元素值
sorted_indexed_list = sorted(indexed_list, key=lambda x: -x[1])
for index in sorted_indexed_list[:10]:
    print(all_combinations[index[0]])
    print(trait_group[index[0]])



# 打印前几个组合作为示例（可选，因为打印所有组合可能会非常庞大）
# for i, combo in enumerate(all_combinations[:10]):  # 这里只打印前10个组合
#     print(f"组合 {i + 1}: {combo}")




