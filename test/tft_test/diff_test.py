#coding=utf-8

'''
Created on 2012-8-14

@author: Huiyugeng
'''
import unittest
import text

'''
diff单元测试
'''
class DiffTest(unittest.TestCase):


    def test_diff_compare(self):
        diff_list = text.diff_file('diff_1.log', 'diff_2.log')
        for diff_item in diff_list:
            print ("%7s a[%d:%d] (%s) b[%d:%d] (%s)" %  (diff_item.get('tag'), 
                                                         diff_item.get('src_start'), diff_item.get('src_end'), diff_item.get('src_item'),
                                                         diff_item.get('dst_start'), diff_item.get('dst_end'), diff_item.get('dst_item'),))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()