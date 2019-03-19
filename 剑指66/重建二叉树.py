# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        T = TreeNode(pre.pop(0))## 每次把根pop出
        index = tin.index(T.val)
        T.left = self.reConstructBinaryTree(pre, tin[:index])
        T.right = self.reConstructBinaryTree(pre, tin[index + 1:]) ##因为此刻左边已经全pop了

        return T