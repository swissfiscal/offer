#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 Created on 2019/3/12
 @author: luomashuzi
 desc:
 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## plan A
        # while '{}' in s or '()'in s or '[]' in s:
        #     s=s.replace('{}','')
        #     s=s.replace('()','')
        #     s=s.replace('[]','')
        # return s==''

        # plan B
        stack = []
        paren_map = { ')': '(', ']':'[', '}':'{'}
        #所有的右括号都放在前面
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif not stack or paren_map[c] != stack.pop():
                return False
        return not stack
if __name__ == '__main__':
    a=Solution()
    print(a.isValid('([[[]]]))'))