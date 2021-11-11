from Generator.helper import listHelper
import random

def __next_type__(word_dict, next_types):

    index_list = []
    listHelper.addFromDict(index_list, word_dict, *next_types)
    index_list.sort()
    rand_index = random.randint(0, len(index_list) - 1)
    return index_list[rand_index]

def __a_sentence__(seq, type_index, word_types, word_dict, word_len):
    try:
        sentence = ''
        i = 1
        while i <= random.randint(1,word_len):
            type_item = word_types[type_index]
            if type_item['type'] == 'quali':
                i -= 1
            data = type_item['data']
            new_word = data[random.randint(0, len(data) - 1)]
            if not new_word in seq:
                sentence += new_word
                type_index = __next_type__(word_dict, type_item['next'])
                i += 1
    except Exception as err:
        pass
    finally:
        return sentence

def run(word_types, rules, sent_len, word_len):
    i = 1
    seq = ''
    
    word_dict = {}
    for index in word_types:
        word_dict[index['type']] = word_types.index(index)
    
    start_rule = []
    for item in rules:
        if item['rule'] == 'start':
            start_rule = item['data']

    while i <= sent_len:
        start_type_index = random.randint(0, len(word_types) - 1)
        start_type = word_types[start_type_index]['type']
        if start_type in start_rule:
            seq_item = __a_sentence__(seq, start_type_index, word_types, word_dict, word_len)
            if len(seq_item) > 0:
                seq += seq_item
            i += 1
            seq += '/'
    return seq.split('/')
