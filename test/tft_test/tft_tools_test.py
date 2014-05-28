#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
import text

'''
tft_tools单元测试
'''
class TxtFileTest(unittest.TestCase):


    def test_property_file(self):
        filename = 'test.cfg'
        config = text.load_property(filename)
        filename = 'test1.cfg'
        text.save_property(filename, config)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()