#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Created on 2019/3/12
 @author: luomashuzi
 desc:
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 各种测试用例
        # strs=["a","","a"]
        # strs=["aa","a"]
        # strs=[]
        # strs=["","","a"]
        # strs=["flower","flow","flight"]
        # strs=["a","a","a"]
        # strs=["dog","racecar","car"]
        comm=''
        if strs==[]:
            return comm
        # 判断是否有空字符串，如果有，一定会返回""
        #  找长度最小的单词,假定第一个最小,挨个比较，断了就换下标
        min=0
        for i in range (len(strs)):
            if len(strs[i])<len(strs[min]):
                min=i
        for i in strs:
            if i=="" or i is None:
                return comm
        # 假设从list中的长度最短的单词的第一个字符，和其他单词的第一个字符对比，如果一样，存储起来并取第二个再和其他的对比，以此类推
        # 第一个对比词
        cmpchar=strs[min][0]
        # 按照最小长度的字符串循环取字符
        for j in  range (len(strs[min])):
            cmpchar=strs[min][j]
            # 循环list长度
            for i in range (len(strs)):
                if cmpchar != strs[i][j]:
                    return comm
            comm+=cmpchar

        return comm
if __name__ == '__main__':
    a=Solution()
    print(a.longestCommonPrefix('["flower","flow","flight"]'))