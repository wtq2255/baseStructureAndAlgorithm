#!/usr/bin/env python
# encoding: utf-8

class Stack():
    def __init__(self, size):
        self.stack = list()
        self.size = size
        self.top = -1

    def push(self, content):
        if self.isFull():
            print 'Stack is full!'
        else:
            self.stack.append(content)
            self.top += 1

    def out(self):
        if self.isEmpty():
            print 'Stack is empty!'
        else:
            self.top -= 1
            return self.stack[self.top + 1]

    def isFull(self):
        return self.size == self.top + 1

    def isEmpty(self):
        return self.top == -1
        
def main():
    s = Stack(1)
    print s.isFull()
    print s.isEmpty()
    s.push('Hello')
    print s.isFull()
    print s.isEmpty()
    print s.top
    print s.out()
    print s.isFull()
    print s.isEmpty()
    print s.top

if __name__ == '__main__':
    main()