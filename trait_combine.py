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
fn = 'chess_message.txt'
fn_1 = 'chess_trait.json'
infn = os.path.join(Config_base.ref,fn)
outfn = os.path.join(Config_base.data_warehouse,fn_1)
aim_dict = {}

with open(infn,'r',encoding='utf_8') as f:
    for line in f:
        mes = line.strip().split("\t")
        print(mes)
        chess_val = mes[0]
        aim_dict[chess_val] = []
        aim_dict[chess_val] = mes[2].split('、')
print(aim_dict)

Config_base.dumps_data(aim_dict,outfn)
# with open(outfn, "w+", encoding='utf-8') as f:
#     f.write(json.dumps(aim_dict, ensure_ascii=False))