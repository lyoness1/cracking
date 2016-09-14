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


# Generic Stack class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []


# 3.2 Write a method get_min() that returns min value in stsack in O(1)
class MinStack:
    def __init__(self):
        self.minStack = Stack()
        self.stack = Stack()

    def push(self, value):
        self.stack.push(value)
        if value <= self.minStack.peek():
            self.minStack.push(value)

    def pop(self):
        data = self.stack.pop()
        if data <= self.minStack.peek():
            self.minStack.pop()
        return data


# 3.3 Set of Stacks that will prevent toppling if stack gets too big
class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            raise Exception("Stack is empty")
        if not self.stacks[-1]:
            self.stacks.remove([])
        return self.stacks[-1].pop()

    def popAt(self, stack_index):
        if not self.stacks:
            raise Exception("Stack is empty")
        if not self.stacks[stack_index]:
            return None
        return self.stacks[stack_index].pop()

# 3.4 











