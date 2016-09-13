# STACKS

# 3.1 Create three stacks from one array
# attributes: single array
# methods: push, pop, peek, isempty
class SingleArrayStacks:
    def __init__(self, stacksize=100, number=3):
        self.stacksize = stacksize
        self.number = number
        self.stack = [None] * self.stacksize * self.number
        self.pointer = [-1] * self.number

    def stacktop(self, stacknum):
        return (stacknum * self.stacksize) + self.pointer[stacknum]

    def push(self, stacknum, value):
        if self.pointer[stacknum] + 1 >= self.stacksize:
            raise Exception("Out of space")
        else:
            self.pointer[stacknum] += 1
            self.stack[self.stacktop(stacknum)] = value

    def pop(self, stacknum):
        if not self.isEmpty(stacknum): 
            data = self.stack[self.stacktop(stacknum)]
            self.stack[self.stacktop(stacknum)] = None
            self.pointer[stacknum] -= 1
            return data
        else:
            raise Exception("Stack is empty")

    def peek(self, stacknum):
        if self.pointer[stacknum] == 1:
            raise Exception("Stack is empty")
        else: 
            return self.stack[self.stacktop(stacknum)]
    
    def isEmpty(self, stacknum):
        return self.pointer[stacknum] == -1



