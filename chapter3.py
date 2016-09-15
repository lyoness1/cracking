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

# 3.4 Towers of Hanoi
# A) Only one disk can be moved at a time
# B) disks can only be placed on larger disks or empty rods
class Hanoi:
    def __init__(self, size):
        self.size = size
        self.towers = [[x for x in xrange(size, 0, -1)],[],[]]

    def moveDisk(self, fr, to):
        disk = self.towers[fr-1].pop()
        self.towers[to-1].append(disk)
    
    def play(self, n, start, temp, end):
        if n == 1:
            self.moveDisk(start, end)
        else: 
            self.play(n-1, start, end, temp)
            self.play(1, start, temp, end)
            self.play(n-1, temp, end, start)


# 3.5 myQueue is a queue with two stacks
class MyQueue:
    def __init__(self):
        self.first = []
        self.second = []

    def nq(self, value):
        self.first.append(value)

    def dq(self):
        if len(self.first) == 0:
            return self.second.pop()
        else: 
            while self.first:
                self.second.append(self.first.pop())
            self.dq()

    def peek(self):
        if len(self.first) == 1:
            return self.first[-1]
        else: 
            while self.first:
                self.second.append(self.fisrt.pop())
            self.peek()

    def get_size(self):
        return len(self.first) + len(first.second)


# 3.6 write a method to sort a stack in ascending order
# Make no assumptions about how the stack is implemented
# Use push(), peek(), pop(), and is_empty() only
class MyStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def sort_in_ascending_order(self):
        old = self
        # make a new stack
        new = MyStack()
        # while the old stack still has things in it...
        while not old.is_empty():
            # grab the top thing from the old stack
            tmp = old.pop()
            # if the new stack isn't empty and its top value is bigger than temp
            # take things off the new stack and put them back on the old one
            while not new.is_empty() and new.peek() > tmp:
                old.push(new.pop())
            # put the temp on the new stack
            new.push(tmp)
            # if the old stack isn't empty and it's top value is bigger than new
            # take things off the old stack and put them on the new one
            while not old.is_empty() and old.peek() >= new.peek():
                old.push(new.pop())
        # return the sorted stack
        return new













