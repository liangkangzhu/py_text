#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
from regex import regex_map

'''
regex_map单元测试
'''
class RegexMapTest(unittest.TestCase):


    def test_reflect(self):
        map_list = regex_map.load_map('regex.map')
        
        line = 'FW log:name=ASA5505;time=2013-07-10;action=permit;value=45'
        print regex_map.reflect(map_list, line)
        
        line = 'WAF;name=ANHENG;time=2013-07-10;action=deny;value=32'
        print regex_map.reflect(map_list, line)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()