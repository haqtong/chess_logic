#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mes_load.py    
@Contact :   hqtong@epsoft.com.cn
@Desciption：
------------ 

------------ 
@Modify Time      @Author    @Version    
------------      -------    --------  
2024/11/21 15:22   hqtong      1.0         
'''

# import lib
import json
fn = r'D:\python_program\chess\s13\chess_library\chess_message_2.txt'
fn_1 = 'chess_val.json'

outfn = os.path.join(Config.path.outpath,fn_1)
aim_dict = {}

with open(fn,'r',encoding='utf_8') as f:
    for line in f:
        mes = line.strip().split("：")
        print(mes)
        chess_val = mes[0]
        aim_dict[chess_val] = []
        aim_dict[chess_val] = mes[1].split('、')
json.load(dict,outfn)