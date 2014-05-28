#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
from regex import regex_rule

import text

'''
regex_rule单元测试
'''
class RegexRuleTest(unittest.TestCase):

    def test_match(self):
        file_content = text.load_file_as_list('regex_rule.log')
        
        rule_list = regex_rule.load_rule('regex.rule')
        result = regex_rule.match(rule_list, file_content)
        print result
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()