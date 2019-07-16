# -*- coding:utf-8 -*-
"""
@author : linchangyu
@date : 2019-4-11
@question :
有一个九宫格抽奖活动，目前有20种奖品可供抽奖，每个奖品的中奖概率不同，在同一时间段内只能有9种奖品进行抽奖活动，
也就是在一段时间内随机挑选9种奖品进行九宫格抽奖，如何能够保证在不同奖品随机搭配后中奖概率相对准确，（比如会
出现的问题：当前的9种商品的中奖概率加起来已经超过了100%，同一时段内的9个奖品概率加起来应该接近100%），请给出
一个解决方案，逻辑说明如何实现。
@thinking :
若九个奖品的概率之和超过100或者不到100，则按照比例将其扩大或缩小即可

-------------------------------------------------------------------------------------------
test output:
随机取9个奖品的概率分别为： [15, 3, 2, 8, 6, 30, 40, 7, 11]
概率之和为： 122 %
处理后9个奖品的概率分别为： [12.295, 2.459, 1.639, 6.557, 4.918, 24.59, 32.787, 5.738, 9.016]
概率之和为： 99.999 %
-------------------------------------------------------------------------------------------

"""
import random
# 假定20件奖品的概率分别为1%-20%，1%用1表示，以此类推
list_probability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 15, 18, 20, 25, 30, 35, 40, 50]
list_random = []
temp = list_probability[random.randint(0, 19)]
while len(list_random) < 9:
    if temp not in list_random:
        list_random.append(temp)
    else:
        temp = list_probability[random.randint(0, 19)]
sum_list_random = sum(list_random)
print "随机取9个奖品的概率分别为：", list_random, "\n概率之和为：", sum_list_random, "%"
ratio = sum_list_random/float(100)
list_res = []
for item in list_random:
    list_res.append(round(item/ratio, 3))
print "处理后9个奖品的概率分别为：", list_res, "\n概率之和为：", sum(list_res), "%"
