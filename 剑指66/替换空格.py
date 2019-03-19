# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = ''
        for i in s:
            if i == ' ':
                new_s += '%20'
            else:
                new_s += i

        return new_s