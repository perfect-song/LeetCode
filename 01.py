'''
盛水最多的容易
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点
分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

'''

###暴力及素颜
class Solution1:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        m = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                if area > m:
                    m = area

        return m

class Solution2:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        考虑计算的容量是索引差与两个索引对于的最小值的乘积，故而，若对应大的值的索引往外移动会增大乘积，
        对应小值的索引往内移动会增大乘积
        """

        if len(height) < 2:
            return 0
        m = 0
        i,j = 0, len(height)-1
        while i<j:
            area = (j - i) * min(height[i], height[j])
            # if area > m:
            #     m = area
            m = max(m, area)
            if (height[i]<height[j]):
                i += 1
            else:
                j -= 1
        return m

h = [1,8,6,2,5,4,8,3,7]

S = Solution2()
# S.maxArea(h)
print(S.maxArea(h))