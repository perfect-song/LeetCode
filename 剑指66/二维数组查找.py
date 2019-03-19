# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        m, n = len(array), 0
        m -= 1
        while (m >= 0 and n < len(array[0])):
            if array[m][n] == target:
                return True
            elif array[m][n] > target:
                m -= 1
            else:
                n += 1
        return False