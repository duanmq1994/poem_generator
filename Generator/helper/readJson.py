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


def insert(jpath, dict_obj):
    '''
    json字典列表写入文件
    '''
    try:
        jfile = os.path.join(PATH, jpath)
        if os.path.exists(jfile):
            os.remove(jfile)
        with open(jfile, 'w', encoding='utf-8') as f:
            json.dump(dict_obj, f, ensure_ascii=False, indent=4)
    except Exception as e:
        return [{"name":str(e)}]