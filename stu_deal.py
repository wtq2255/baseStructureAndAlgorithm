#!/usr/bin/env python 
# coding: utf-8

# 在 stu_deal.txt 中保存学生的信息
# 12345,张三
# 12346,李四
# ...
# （学号唯一）
# 现要加入一个学生信息

import os

class Student(object):
    """定义学生类"""
    def __init__(self, sId, sName):
        self._sId = sId
        self._sName = sName

    @property
    def sId(self):
        return self._sId
    @sId.setter
    def sId(self, sId):
        self._sId = sId

    @property
    def sName(self):
        return self._sName
    @sName.setter
    def sName(self, sName):
        self._sName = sName

class Manage(object):
    """docstring for Manage"""
    def __init__(self, fileName):
        self.fileName = fileName

    def isNone(self):
        if os.path.exists(os.getcwd() + os.sep + self.fileName):
            with open(self.fileName) as f:
                if len(f.read()) != 0:
                    return True
        return False

    def readFile(self):
        resultDic = dict()
        if self.isNone():
            with open(self.fileName, 'rt') as f:
                s = f.readline()
                l = s.split(',')
                resultDic[l[0]] = l[1]
        return resultDic

    def writeFile(self, dic):
        with open(self.fileName, 'wt') as f:
            for (key, val) in dic.iteritems():
                s = (','.join([key, val])) + '\n'
                f.write(s)
        print 'done'

    def dealDic(self, dic, stu):
        dic[stu.sId] = stu.sName
        return dic


def main():
    m = Manage('stu_deal.txt')
    dic = m.readFile()
    for x in xrange(1,10):
        s = Student(str(x), '李四')
        dic = m.dealDic(dic, s)
    m.writeFile(dic)
    # print m.isNone()

if __name__ == '__main__':
    main()
