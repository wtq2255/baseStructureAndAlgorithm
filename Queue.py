#!/usr/bin/env python
# coding: utf-8

class Queue():
    '''实现队列结构'''
    def __init__(qu,size):
        '''初始化队列，并设置队列大小'''
        qu.queue = list()
        qu.size = size
        qu.head = -1
        qu.tail = -1

    def isFull(qu):
        '''返回队列是否已满'''
        return qu.tail - qu.head == qu.size

    def isEmpty(qu):
        '''返回队列时候为空'''
        return qu.tail == qu.head

    def enQueue(qu, content):
        '''入队操作'''
        if qu.isFull():
            print 'Queue is full'
        else:
            qu.queue.append(content)
            qu.tail += 1

    def deQueue(qu):
        '''出队操作'''
        if qu.isEmpty():
            return 'Queue is empty'
        else:
            qu.head += 1
            return qu.queue[qu.head]


def main():
    q = Queue(1)
    print 'isFull', q.isFull()
    print 'isEmpty', q.isEmpty()
    q.enQueue('Hello')
    q.enQueue('Hello')
    print 'isFull', q.isFull()
    print 'isEmpty', q.isEmpty()
    print q.deQueue()
    print q.deQueue()
    print 'isFull', q.isFull()
    print 'isEmpty', q.isEmpty()
        
if __name__ == '__main__':
    main()