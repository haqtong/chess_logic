#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mes_load.py    
@Contact :   hqtong@epsoft.com.cn
@Desciption：
------------ 
chess_val
------------ 
@Modify Time      @Author    @Version    
------------      -------    --------  
2024/11/21 15:22   hqtong      1.0         
'''
# import lib
import json
import os
from config.set_config import *
fn = 'chess_trait.json'
fn_1 = 'trait_chess_group.json'
infn = os.path.join(Config_base.data_warehouse,fn)
outfn = os.path.join(Config_base.data_warehouse,fn_1)
chess_trait = Config_base.read_data(infn)
aim_dict = {}
trait_tmp = []
for chess,trait_list in chess_trait.items():
    for trait in trait_list:
        trait_tmp.append(trait)
base_trait = list(set(trait_tmp))
for trait in base_trait:
    aim_dict[trait] = []

for chess,trait_list in chess_trait.items():
    for trait in trait_list:
        aim_dict[trait].append(chess)

Config_base.dumps_data(aim_dict,outfn)
