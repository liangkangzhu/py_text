#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
import text

'''
grep单元测试
'''
class QueryTest(unittest.TestCase):


    def test_grep(self):
        _list = ['hello world', 'hello girl', 'just want to say hello', 'no he', 'no hell']
        print text.grep('hello', _list, '', True)
        
        print text.grep('mkdir', 'test.shell', '', True)
        
        print text.grep('[1,3]', 'test.shell', 'N', True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()