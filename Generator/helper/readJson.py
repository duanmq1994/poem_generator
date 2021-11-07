import json
import os
PATH = os.path.dirname(os.path.abspath(__file__))

def read(jpath):
    '''
    读取json文件，获取json字典列表
    '''
    try:
        jfile = os.path.join(PATH, jpath)
        with open(jfile, 'rb') as f:
            json_dict = json.load(f)
            return json_dict
    except Exception as e:
        return [{"name":str(e)}]