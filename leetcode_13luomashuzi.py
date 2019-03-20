#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Created on 2019/3/12
 @author: luomashuzi
 desc:
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        di={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # print(di['I'])
        sum=0
        for index in range(len(s)-1,-1,-1):
            print('index',index)
            print(s[index])
            if index==len(s)-1:
                sum =sum + di[s[index]]
            elif di[s[index]]<di[s[index+1]]:
                sum =sum - di[s[index]]
            else:
                sum =sum + di[s[index]]
        return sum

if __name__ == '__main__':
    a=Solution()
    print(a.romanToInt('III'))