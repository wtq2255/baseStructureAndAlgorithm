#!/usr/bin/env python
# coding: utf-8

class Queue():
    def __init__(qu,size):
        qu.queue = list()
        qu.size = size
        qu.head = -1
        qu.tail = -1

    def isFull(qu):
        return qu.tail - qu.head == qu.size

    def isEmpty(qu):
        return qu.tail == qu.head

    def enQueue(qu, content):
        if qu.isFull():
            print 'Queue is full'
        else:
            qu.queue.append(content)
            qu.tail += 1

    def deQueue(qu):
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