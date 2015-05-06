#coding=utf-8

'''
文本文件操作工具

@author: Huiyugeng
'''

'''
载入文件为一个列表（针对UTF-8文本文件）

@param filename: 需要载入的文件名

@return: 文本文件内容列表 
'''
def load_file_as_list(filename):
    file_info = []
    try:
        _file = open(filename, 'r')
        file_info = [line for line in _file.readlines() if line!=""]
        _file.close()
    except IOError:
        file_info = None
    return file_info

'''
保存文件内容
@param filename: 需要保存的文件名
@param file_content_list: 需要保存的文件内容(列表形式)  
'''
def save_file(filename, file_content_list):
    try:
        _file = open(filename, 'w')
        for line in file_content_list:
            _file.write(line)
        _file.close()
    except IOError:
        pass

'''
载入文件内容（针对UTF-8文本文件）

@param filename: 需要载入的文件名

@return: 文本文件内容 
'''
def load_file(filename):
    file_info = ''
    try:
        _file = open(filename, 'r')
        file_info = ''.join(_file.readlines())
        _file.close()
    except IOError:
        file_info = None
    return file_info

'''
载入配置文件（仅支持UTF-8文本文件）
配置文件采用 key = value的形式
支持"#"作为注释符

@param filename: 配置文件

@return: key-value模式配置内容 
'''
def load_property(filename, use_comment=False):
    config = {}
    try:
        _file = open(filename , 'r')
        comment = ''
        for line in _file.readlines():
            line = line.strip()
            if line.startswith('#') == False and line != '':
                key, value = line.split('=')
                if use_comment :
                    config[key] = {}
                    config[key]['value'] = value.strip()
                    if comment != '':
                        config[key]['comment'] = comment
                        comment = ''
                else:
                    config[key] = value.strip()
            else:
                comment = line[1:len(line)]
        _file.close()
    except IOError:
        config = None
    return config

'''
保存配置文件

@param filename: 配置文件名
@param config: key-value模式配置内容 和注释内容
'''
def save_property(filename, config):
    try:
        _file = open(filename, 'w')
        for key in config.keys():
            _config_item = config.get(key)
            if isinstance(_config_item, dict):
                if _config_item.has_key('comment'):
                    _file.write('#{0}\n'.format(_config_item.get('comment')))
                if _config_item.has_key('value'):
                    _file.write('{0}={1}\n'.format(key, _config_item.get('value')))
            else:
                _file.write('{0}={1}\n'.format(key, _config_item))
        _file.close()
    except IOError:
        pass

    
