# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:29:59 2016

@author: ysingh2
"""
import json
import requests


def postFluent(Val1,Val2):
    payload={"json": json.dumps({"Val1":Val1,"Val2":Val2})}
    url='http://127.0.0.1:8888/collectd'
    r= requests.post(url, data= payload)
    print('sent')