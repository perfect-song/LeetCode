# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here

        '''
        斐波那契数列

        :param number:
        :return:
        '''
        if number == 0:
            return 0
        l = [1, 2]
        for i in range(2, number):
            l.append(l[i - 1] + l[i - 2])

        return l[number - 1]