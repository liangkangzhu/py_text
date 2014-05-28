#coding=utf-8

'''
Created on 2013年7月13日

@author: huiyugeng
'''

import ndb

import regex
import text

'''
载入规则映射
'''
def load_rule(rule_file):
    rule_struct = ndb.load(rule_file)
    rule_list = ndb.execute(rule_struct, 'select:rule')
    
    return rule_list

'''
规则匹配
'''
def match(rule_list, lines):
    
    result = {}
    
    if lines == None:
        return None
    
    for rule_item in rule_list:
        
        match_result = {}
        
        name = rule_item.get('name')
        exp_list = ndb.execute(rule_item, 'select:item')
        for exp_item in exp_list:
            exp_name = exp_item.get('name').strip() if exp_item.has_key('name') else ''
            exp_type = exp_item.get('type').strip() if exp_item.has_key('type') else ''
            exp_pattern = exp_item.get('pattern').strip() if exp_item.has_key('pattern') else ''
            exp_function = exp_item.get('function').strip() if exp_item.has_key('function') else ''
            
            match_result[exp_name] = __is_match(lines, exp_function, exp_pattern, exp_type)
        
        expect = rule_item.get('expect')
        for key in match_result:
            expect = expect.replace(key, str(match_result.get(key)))
        
        result[name] = eval(expect)

    return result

def __is_match(lines, exp_function, exp_pattern, exp_type):
    result = False
    
    if regex.check_line('(.*)\((.*)\)', exp_function):
        fun, value = regex.get_line('(.*)\((.*)\)', exp_function)
        
        fun = fun.strip()
        value = value.strip()
        model = 'N' if exp_type == 'line' else 'E'

        result_lines = text.grep(exp_pattern, lines, model)
        if fun == 'match':
            result = result_lines != None and len(result_lines) > 0
        elif fun == 'count':
            if str.isdigit(value) == True:
                count = int(value)
                result = result_lines != None and len(result_lines) == count
        elif fun == 'range':
            if len(value) >= 3 and ',' in value:
                region = value.split(',')
                if len(region) == 2: 
                    _min = int(region[0].strip())
                    _max = int(region[1].strip())
                    result =  len(result_lines) >= _min and len(result_lines) <= _max
    
    return result
