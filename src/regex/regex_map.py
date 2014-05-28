#coding=utf-8

'''
Created on 2013年7月13日

@author: huiyugeng
'''
import types

import ndb

import regex

'''
载入解析映射
'''
def load_map(map_file):
    map_struct = ndb.load(map_file)
    map_list = ndb.execute(map_struct, 'select: map')

    return map_list

'''
规则匹配及字段映射
'''
def reflect(map_list, line):
    value_list = []
    map_index = {}
    
    if line == None:
        return None
    
    line = line.strip()
    
    for map_item in map_list:
        rule_type = map_item.get('type').strip() if map_item.has_key('type') else ''
        if rule_type == '':
            rule_type = 'regex'
        pattern = map_item.get('pattern') if map_item.has_key('pattern') else ''
        
        if rule_type == 'regex':
            if regex.check_line(pattern, line):
                value_list = regex.get_line(pattern, line)
                map_index = __build_map_index(map_item)
                break
        
        elif rule_type == 'split':
            match = map_item.get('match') if map_item.has_key('match') else ''
            if __is_match(match, line):
                value_list = line.split(pattern)
                map_index = __build_map_index(map_item)
                break
            
    map_value = {}
    index = 1
    for value in value_list:
        key = map_index.get(str(index))
        if key != None:
            map_value[key] = value
        index = index + 1
        
    return map_value
                
    
def __build_map_index(map_item):
    map_index = {}
    
    map_index_list = map_item.get('item') if map_item.has_key('item') else []
        
    for _map_index in map_index_list:
        try:
            if _map_index.has_key('index') and _map_index.has_key('key'):
                map_index[_map_index.get('index')] = _map_index.get('key')
        except:
            pass
    
    return map_index

def __is_match(match, line):
    result = False
    
    if regex.check_line('(\S+)\((\S+)\)', match):
        fun, value = regex.get_line('(\S+)\((\S+)\)', match)
        if fun == 'startswith':
            result = line.startswith(value)
        elif fun == 'endswith':
            result = line.endswith(value)
        elif fun == 'in':
            result = value in line
    
    return result
