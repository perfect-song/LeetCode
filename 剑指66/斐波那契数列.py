# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        '''

        第一种递归 但是容易超时
        :param n:
        :return:
        '''
        #        if n==0:
        #            return 0
        #        elif n==1 or n==2:
        #            return 1
        #        else:
        #            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

        '''
        动态规划 1
        '''
        # f, g = 0, 1
        # while (n > 0):
        #     g = g + f
        #     f = g - f
        #     n -= 1
        # return f

        '''
        
        动态规划2  用空间复杂度代替时间复杂度
        '''
        record = [0, 1, 1]
        # if n<=2:
        #     return record[n]
        for i in range(3,n+1):
            record.append(record[i-1] + record[i-2])
        return record[n]

c = Solution()
print(c.Fibonacci(5))