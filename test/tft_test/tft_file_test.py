#coding=utf-8

'''
tft_file单元测试

@author: Huiyugeng
'''
import unittest
import text

class TxtFileTest(unittest.TestCase):


    def test_property_file(self):
        filename = '../../resource/test.cfg'
        config = text.load_property(filename)
        filename = '../../resource/test_new.cfg'
        text.save_property(filename, config)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()