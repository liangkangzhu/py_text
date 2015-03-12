#coding=utf-8

'''
内容对比工具

@author: Huiyugeng
'''
import difflib

'''
对比两个文本文件之间的不同

@param src_filename: 源文件
@param dst_filename: 目标文件 

@return: 文件内容的不同
'''
def diff_file(src_filename, dst_filename):
    
    src_file = file(src_filename, 'r')
    dst_file = file(dst_filename, 'r')
    src_file_context = src_file.read()
    dst_file_context = dst_file.read()
    src_file_context = src_file_context.splitlines()
    dst_file_context = dst_file_context.splitlines()
    
    return diff_text(src_file_context, dst_file_context)

'''
对比两个字符串

@param src_context: 源字符串内容
@param dst_context: 目标字符串内容  

@return: 两个字符串的不同
'''  
def diff_text(src_context, dst_context):
    seq_matcher = difflib.SequenceMatcher(None, src_context, dst_context)
    diff_list = []
    for tag, src_start, src_end, dst_start, dst_end in seq_matcher.get_opcodes():
        diff_result = {}
        diff_result['tag'] = tag
        diff_result['src_start'] = src_start
        diff_result['src_end'] = src_end
        diff_result['src_item'] = src_context[src_start : src_end]
        diff_result['dst_start'] = dst_start
        diff_result['dst_end'] = dst_end
        diff_result['dst_item'] =  dst_context[dst_start : dst_end]
        
        diff_list.append(diff_result)
        
    return diff_list

