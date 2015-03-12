#coding=utf-8

'''
基于正则表达式的规则匹配单元测试

@author: Huiyugeng
'''
import unittest
from regex import regex_rule

'''
regex_rule单元测试
'''
class RegexRuleTest(unittest.TestCase):

    def test_match(self):
        file_content = ['FW log:name=ASA5505;time=2013-07-10;action=permit;value=45', 
                        'FW log:name=ASA5505;time=2013-07-10;action=permit;value=45',
                        'FW log:name=ASA5505;time=2013-07-10;action=permit;value=45']
        
        rule_list = regex_rule.load_rule('../../resource/regex.rule')
        result = regex_rule.match(rule_list, file_content)
        print result
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()