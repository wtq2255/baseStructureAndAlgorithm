#!/usr/bin/env python
# coding: utf-8

class Node:
    """单链表中的节点"""
    def __init__(self, data, p = 0):
        # 数据数据
        self.data = data
        # 存储下一节点地址
        self.next = p

class LinkedList:
    """实现一个单链表结构"""
    def __init__(self):
        # 初始化单链表头
        self.head = 0

    def initWithList(self, datas):
        '''初始化单链表'''
        self.head = Node(datas[0])
        p = self.head
        for data in datas[1:]:
            n = Node(data)
            p.next = n
            p = n

    def getLength(self):
        '''获取单链表长度'''
        length = 0
        p = self.head
        while p != 0:
            length += 1
            p = p.next
        return length

    def isEmpty(self):
        '''返回单链表是否为空'''
        if self.getLength == 0:
            return True
        else:
            return False

    def append(self, val):
        '''向单链表添加元素'''
        n = Node(val)
        p = self.head
        if self.isEmpty():
            p = n
        else:
            while p.next != 0:
                p = p.next
            p.next = n

    def insert(self, index, val):
        '''在 index 处插入元素'''
        if index < 0 or index > self.getLength():
            return 'index is error'
        if self.isEmpty() and index != 0:
            return 'LinkedList is empty, so index must be 0'

        p = self.head
        post = self.head

        if index == 0:
            self.head = Node(val, p)
            return

        
        j = 0

        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if j == index:
            n = Node(val, p)
            post.next = n
            return
        return 'index is error'



    def printl(self):
        '''打印单链表'''
        p = self.head
        if p == 0:
            return "LinkedList is Empty"
        while p != 0:
            print(p.data)
            p = p.next

linkedList = LinkedList()
linkedList.initWithList([1,2,3,4])
print '长度为: ', linkedList.getLength()
linkedList.printl()
linkedList.append(5)
linkedList.printl()
print '------'
linkedList.insert(3, 10)
linkedList.insert(0, 10)
linkedList.printl()

        
