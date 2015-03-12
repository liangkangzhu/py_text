#coding=utf-8

'''
awk单元测试

@author: Huiyugeng
'''
import unittest
import text


class AwkTest(unittest.TestCase):


    def test_awk(self):
        _list = ['1:huyugeng:male', '2:zhuzhu:male', '3:maomao:fmale', '4:tiantian:male', '5:tongtong:fmale']
        print text.awk('', _list, ':', None)
        
        print text.awk('', _list, ':', [0, 2])
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()