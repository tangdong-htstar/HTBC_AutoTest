'''
工具函数模块，包含一些常用的工具函数，如数据处理、文件读取等
'''

import yaml

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)