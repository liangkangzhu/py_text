'''
Created on 2013-2-24

@author: Huiyugeng
'''
import difflib

'''
compare differnet between two files
@param src_filename: Source Filename
@param dst_filename: Destination Filename  

@return: two files differents
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
compare differnet between two string
@param src_context: Source Context
@param dst_context: Destination Context  

@return: two string differents
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

