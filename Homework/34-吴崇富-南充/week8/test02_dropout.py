#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
函数中，x是本层网络的激活值。Level就是每个神经元要被丢弃的概率。
'''
import numpy as np
# dropout函数的实现
def dropout(x,level):
    if level < 0 or level >= 1: #level是概率值，必须在0~1之间
        raise ValueError('Dropout level must be in interval [0,1].')
    retain_prob = 1. - level
    # 通过binomial函数(二项式分布函数)，生成与x一样的维数向量。binomial函数就像抛硬币一样，我们可以把每个神经元当做抛硬币一样
    # 硬币 正面的概率为p，n表示每个神经元试验的次数
    # 因为我们每个神经元只需要抛一次就可以了所以n=1，size参数是我们有多少个硬币。
    random_tensor = np.random.binomial(n=1,p=retain_prob,size=x.shape) #即将生成一个0、1分布的向量，0表示这个神经元被屏蔽，不工作了，也就是dropout了
    print(random_tensor)

    x *= random_tensor
    print(x)
    return x

#自造输入数据x
'''
np.array与np.asarray的区别，其在于输入为数组时，np.array是将输入copy过去而np.asarray是将输入cut过去，
所以随着输入的改变np.array的输出不变，而np.asarray的输出在变化，
并且当我们使用np.asarray改变其类型的时候(输入是float64，改为float32)，这样当输入改变的时候，np.asarray的输出也不会改变。
'''
x = np.asarray([1,2,3,4,5,6,7,8,9,10],dtype=np.float32)
dropout(x,0.4)