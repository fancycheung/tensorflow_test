# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:59:57 2017

@author: zhangfangxi
"""

import tensorflow as tf

def add():
    '''加法尝试'''
    a = tf.constant([1.0,2.0],name="aa")
    b = tf.constant([2.0,3.0],name="bb")
    return a+b

add()
