#coding=utf-8

'''
Created on 2015-2-5

@author: Huiyugeng

Regex Toolset
'''

import regex
import regex_map
import regex_rule

def get_line(regex_str ,line):
    return regex.get_line(regex_str, line)

def check_line(regex_str, line):
    return regex.check_line(regex_str, line)