#coding=utf-8

'''
tft_file单元测试

@author: Huiyugeng
'''
import unittest
import text

class TftFileTest(unittest.TestCase):

    def test_property_file(self):
        filename = '../../resource/test.cfg'
        config = text.load_property(filename, True)
        print config
        text.save_property('../../resource/test_comment.cfg', config)
        
        config = text.load_property(filename, False)
        print config
        text.save_property('../../resource/test_no_comment.cfg', config)
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()