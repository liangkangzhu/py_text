#coding=utf-8

'''
python grep工具

@author: Huiyugeng
'''
import regex
import types
import tft_file

'''
grep功能

@param regex_exp: 正则表达式，
@param target：需要匹配的目标，list或文件名，
@param model： 模式, E为正则表达式模式，N为行数模式（支持负行数），
@param number： 是否显示行数

@return 处理后的行
'''
def grep(regex_exp, target, model, number=False):
    count = 1;
    _list = __list(target)
    
    result = []
    
    if model == 'N':
        _min, _max = __split_region(regex_exp)
            
    for text in _list:
        if model == None or model == '' or model == 'S':
            if regex_exp in text:
                result.append(__print(count, text, number))
        elif model == 'N':
            if len(text) > 3: 
                if count >= _min and count <= _max:
                    result.append(__print(count, text, number))
        elif model == 'E':
            if regex.check_line(regex_exp, text):
                result.append(__print(count, text, number))
        count = count + 1
    
    return result

'''
判断正则表达式中描述的行数
'''
def __split_region(regex_exp):
    if regex_exp.startswith('[') and regex_exp.endswith(']') and ',' in regex_exp:
        region = regex_exp[1: len(regex_exp) - 1].split(',')
        _min = int(region[0])
        _max = int(region[1])
        return _min, _max

'''
将目标转换为列表
'''        
def __list(target):
    _list = []
    if type(target) == types.ListType:
        _list = target
    elif type(target) == types.StringType:
        _list = tft_file.load_file_as_list(target)
    
    return _list

'''
输出内容
'''
def __print(count, text, number):
    if number:
        return (str(count) + ':' + text.strip())
    else:
        return text.strip()
    
