#!/usr/bin/env python
# encoding: utf-8

class Stack():
    '''实现栈结构'''
    def __init__(self, size):
        '''初始化栈，并设置其大小'''
        self.stack = list()
        self.size = size
        self.top = -1

    def push(self, content):
        '''压栈操作'''
        if self.isFull():
            print 'Stack is full!'
        else:
            self.stack.append(content)
            self.top += 1

    def out(self):
        '''出栈操作'''
        if self.isEmpty():
            print 'Stack is empty!'
        else:
            self.top -= 1
            return self.stack[self.top + 1]

    def isFull(self):
        '''返回栈是否已满'''
        return self.size == self.top + 1

    def isEmpty(self):
        '''返回栈是否为空'''
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