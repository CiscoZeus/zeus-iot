# -*- coding: utf-8 -*-
"""
Created on Wed May 04 23:40:36 2016

@author: ysingh2
"""

from zeus import client as zc

z= zc.ZeusClient('f0069791', 'api.ciscozeus.io')

def Metricsend(a,name,ts):
    metric = [{"timestamp":ts, "point":{"value":a}}]
    z.sendMetric(name,metric)
    print "."
    
    
    

    