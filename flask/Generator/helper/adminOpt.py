from Generator.helper import readJson

def check_word(word_types, word):
    '''
    检查重复词汇
    '''
    for word_type in word_types:
        if word in word_type['data']:
            return '该词已存在。'
    return 'ok'

def add_word(word_types, json_path, change_type, word):
    '''
    新增词汇
    '''
    for word_type in word_types:
        if word_type['type'] == change_type:
            word_type['data'].append(word)
    readJson.rewrite(json_path, word_types)


def update_type(word_types, json_path, type_name, next_types, end):
    '''
    修改类型
    '''
    if end == 'on':
        next_types.append('end')

    for word_type in word_types:
        if word_type['type'] == type_name:
            word_type['next'] = next_types
            readJson.rewrite(json_path, word_types)
            return

    new_type = {}
    new_type['type'] = type_name
    new_type['data'] = []
    new_type['next'] = next_types

    word_types.append(new_type)
    readJson.rewrite(json_path, word_types)

def update_start_rule(rules, rule_path, type_name, start):
    '''
    添加开头规则
    '''
    for rule in rules:
        if rule['rule'] == 'start':
            if (not type_name in rule['data']) and (start == 'on'):
                rule['data'].append(type_name)
            elif (type_name in rule['data'] and (start != 'on')):
                rule['data'].remove(type_name)
    readJson.rewrite(rule_path, rules)

def delete_type(word_types, json_path, rules, rule_path, type_name):
    '''
    删除类型
    '''
    for word_type in word_types:
        if word_type['type'] == type_name:
            word_types.remove(word_type)
        else:
            if type_name in word_type['next']:
                word_type['next'].remove(type_name)
    readJson.rewrite(json_path, word_types)

    for rule in rules:
        if type_name in rule['data']:
            rule['data'].remove(type_name)
    readJson.rewrite(rule_path, rules)