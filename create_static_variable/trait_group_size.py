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
fn = 'trait_chess_group.json'
fn_1 = 'trait_chess_group_size.json'
infn = os.path.join(Config_base.data_warehouse,fn)
outfn = os.path.join(Config_base.data_warehouse,fn_1)
trait_group = Config_base.read_data(infn)
print(trait_group)
aim_dict = {}

for trait,chess_group in trait_group.items():
    aim_dict[trait] = []

Config_base.dumps_data(aim_dict,outfn)
