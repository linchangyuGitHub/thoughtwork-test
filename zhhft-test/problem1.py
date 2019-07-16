# -*- coding:utf-8 -*-
"""
@author : linchangyu
@date : 2019-4-11
@question:
有一个数组a，要求写一个方法，将这个数组拆分为两个子数组，要求两个子数组内的变量之和尽可能接近：
@thinking :
动态规划dp
转换为0/1背包问题后可快速判断出对于中间值target数组是否存在一个子序列和为该值，
若不存在可递归判断target = target - 1
但存在问题是得到存在子序列符合条件这一结论后不好直接给出对应的子序列
所以采用穷举法动态判断最优解，时间复杂度O(n2)
经测试25个元素以内可较快给出答案
后续可以采用深搜+剪枝的方式优化
暂时没有想到逻辑正确且复杂度低一个维度的解决方案

---------------------------------------------------------------------------------------------------------------
test output:
测试数组为 :  [468, 779, 415, 925, 998, 56, 765, 827, 539, 251, 744, 853, 18, 317, 401, 295, 521, 832, 797, 375]
数组和为  11176 中间值为  5588
数组1为 :  [925, 56, 251, 744, 853, 18, 317, 401, 295, 521, 832, 375]
数组和为  5588
数组2为 :  [468, 779, 415, 998, 765, 827, 539, 797]
数组和为  5588
---------------------------------------------------------------------------------------------------------------

"""
import random
import itertools

# Number of test cases
count = 20
t_list = []
for x in range(count):
    t_list.append(random.randint(1, 1000))
target = sum(t_list)/2
print "测试数组为 : ", t_list, "\n数组和为 ", sum(t_list), "中间值为 ", target
tuple_temp = ()
tuple_sum_temp = 1000 * 20
for k in range(1, count):
    for i in itertools.combinations(t_list, k):
        tuple_sum = sum(i)
        medium_tuple_sum = abs(target - tuple_sum)
        if medium_tuple_sum <= tuple_sum_temp:
            tuple_sum_temp = medium_tuple_sum
            tuple_temp = i

list_a = list(tuple_temp)
for m in tuple_temp:
    t_list.remove(m)
print "数组1为 : ", list_a, "\n数组和为 ", sum(list_a)
print "数组2为 : ", t_list, "\n数组和为 ", sum(t_list)


