class stack():
    def __init__(self):
        self.s = []
    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

##对栈实现队列
class Solution():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        while(not self.stack2):
            self.stack1.append(self.stack2.pop())
        self.stack1.append(node)
    def pop(self):

        if len(self.stack2)==0:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

