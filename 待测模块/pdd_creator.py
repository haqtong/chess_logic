# encoding=utf-8
import logging
import itertools
from collections import Counter
from config.set_config import *
import pandas as pd
import datetime
import numpy as np
import os
import sys

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='short_term.log', level=logging.INFO, format=LOG_FORMAT)


class chess():
    def __init__(self):
        self.chess_trait_fn = 'chess_trait.json'
        self.chess_val_fn = 'chess_val.json'
        self.chess_trait_group_fn = 'trait_chess_group.json'
        self.chess_trait_group_size_fn = 'trait_chess_group_size.json'
        self.chess_trait = Config_base.read_data(os.path.join(Config_base.data_warehouse,self.chess_trait_fn))
        self.chess_val = Config_base.read_data(os.path.join(Config_base.data_warehouse,self.chess_val_fn))
        self.chess_trait_group = Config_base.read_data(os.path.join(Config_base.data_warehouse,self.chess_trait_group_fn))
        self.chess_trait_group_size = Config_base.read_data(os.path.join(Config_base.data_warehouse,self.chess_trait_group_size_fn))

    def jbscq(self,lst_0 = [],lst_1 = [],cnt_list = [5,2,7] ):
        '''
        羁绊生成器
        :return:
        '''
        trait_group = {}
        group_size = []
        new_comb = []
        comb_0 = itertools.combinations(lst_0,cnt_list[0])
        comb_1 = itertools.combinations(lst_1, cnt_list[1])
        comb = itertools.product(comb_0,comb_1)
        trait_group = {}
        group_size = []
        for ind, group in enumerate(comb):
            group_new = list(group[0])
            group_new.extend(group[1])
            new_comb.append(group_new)

        for ind, group in enumerate(new_comb):
            tmp_trait = []
            for chess in group:
                tmp_trait.extend(self.chess_trait[chess])
            trait_group[ind] = dict(Counter(tmp_trait))
            for key, val in dict(Counter(tmp_trait)).items():
                if val < self.chess_trait_group_size[key][0]:
                    trait_group[ind].pop(key)

            group_size.append(len(trait_group[ind].keys()))
        # 创建一个包含元素及其原始索引的元组列表
        indexed_list = list(enumerate(group_size))
        print(indexed_list)
        # 对新列表进行排序，排序依据是元素值
        sorted_indexed_list = sorted(indexed_list, key=lambda x: -x[1])
        print(len(sorted_indexed_list))
        for index in sorted_indexed_list[:10]:

            print(new_comb[index[0]])
            print(trait_group[index[0]])

        return 0
    def ylzdyw_creator(self,file_path = os.path.join(Config_base.data_warehouse,'ylzdyw.json') ):
        '''
        意料中的意外表单构建
        :return:
        '''
        aim_dict = {}
        dice = [x for x in range(1, 7)]
        all_sample = itertools.product(dice, dice, dice)
        new_sample_tmp_0 = [sorted(list(x)) for x in all_sample]
        new_sample_tmp_1 = []
        for group in new_sample_tmp_0:
            dice_group ='-'.join([str(x) for x in group])
            new_sample_tmp_1.append(dice_group)

        new_sample_tmp = list(set(new_sample_tmp_1))
        for group in new_sample_tmp:
            aim_dict[group] = []
        Config_base.dumps_data(aim_dict, file_path)
    def ylzdyw(self):
        '''
        意料之中的意外
        :return:
        '''
        file_path = os.path.join(Config_base.data_warehouse,'ylzdyw.json')
        if os.path.exists(file_path):
            print(f"文件 '{file_path}' 存在.")
            aim_dict = Config_base.read_data(file_path)
        else:
            self.ylzdyw_creator(file_path)

        print('请输入要补充的投掷')
        _ = input()
        print('请输入获得的效果')
        _1 = input()
        aim_dict[_].append(_1)
        Config_base.dumps_data(aim_dict,file_path)




        # print(aim_dict)



if __name__ == '__main__':
    chess_class = chess()
    chess_class.ylzdyw_creator()

