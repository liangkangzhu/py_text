#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
import text

'''
awk单元测试
'''
class AwkTest(unittest.TestCase):


    def test_awk(self):
        _list = ['1:huyugeng:male', '2:zhuzhu:male', '3:maoma:fmale', '4:tiantian:male', '5:tongtong:fmale']
        print text.awk('', _list, ':', None)
        
        print text.awk('', _list, ':', [0, 2])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()