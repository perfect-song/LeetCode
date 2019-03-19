# -*- coding:utf-8 -*-

'''
直接返回最小值 使用min函数

'''


class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        rotateArray = list(rotateArray)
        if rotateArray:
            index = rotateArray.index(min(rotateArray))
            # return rotateArray[index:].extend(rotateArray[:index])
            return rotateArray[index]

            pass
        else:
            return 0


'''
先排序 返回第一个元素
'''

class Solution2:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        rotateArray = list(rotateArray)
        if rotateArray:
            rotateArray.sort()
            return rotateArray[0]
        else:
            return 0


'''
二分查找
'''


class Solution3:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        rotateArray = list(rotateArray)

        length = len(rotateArray)

        if length == 0:
            return 0
        i, j = 0, length - 1
        while (i < j):

            if rotateArray[i] < rotateArray[j]:
                return rotateArray[i]

            # m = i + (i - j) // 2
            m = (i + j) // 2
            if rotateArray[i] < rotateArray[m]:
                i = m + 1
            elif rotateArray[j] > rotateArray[m]:
                j = m
            else:
                i += 1

        return rotateArray[i]
