# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        '''
        递归超超时

        就是斐波那契数列
        因为输入n的时候，可以考虑在n-1时走一个或者n-2走两格
        '''
        #        if number==1:
        #            return 1
        #        elif number==2:
        #            return 2
        #        else:
        #            return self.jumpFloor(number-1) + self.jumpFloor(number-2)
        l = [1, 2]
        for i in range(2, number):
            l.append(l[i - 1] + l[i - 2])

        return l[number - 1]
