#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
import text

'''
sed单元测试
'''
class SedTest(unittest.TestCase):


    def test_sed(self):
        _list = ['1:huiyugeng:male', '2:zhuzhu:male', '3:maoma:fmale', '4:tiantian:male', '5:tongtong:fmale']
        print text.sed('.*huiyugeng.*', 'E', 'yugeng.hui', _list, 'R', 'RT')

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()