# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 1  2  4  8  16  32
        '''
        1  2  4  8  16  32
        前n-1项和加1

        f(n) = 2*f(n-1)
        '''
        l = [1, 2]
        for i in range(2, number):
            l.append(sum(l) + 1)
        return l[number - 1]