from Generator.helper import readJson, listHelper
import random

# 每行词数范围
# SENT_MIN = 5
# SENT_MAX = 5
# 行数范围
# WORD_MIN = 3
# WORD_MAX = 10

word_types = readJson.read('../json/words.json')
word_dict = {}
for i in word_types:
    word_dict[i['type']] = word_types.index(i)

def __next_type__(type_name):
    index_list = []
    if type_name == 'num':
        listHelper.addFromDict(index_list, word_dict, 'quali')
    if type_name == 'quali':
        listHelper.addFromDict(index_list, word_dict, 'noun', 'adj', 'verb')
    if type_name == 'noun':
        listHelper.addFromDict(index_list, word_dict, 'verb')
    if type_name == 'verb':
        listHelper.addFromDict(index_list, word_dict, 'verb', 'noun', 'conj')
    if type_name == 'adj':
        listHelper.addFromDict(index_list, word_dict, 'noun')
    if type_name == 'conj':
        listHelper.addFromDict(index_list, word_dict, 'noun', 999)
    index_list.sort()
    rand_index = random.randint(0, len(index_list) - 1)
    return index_list[rand_index]

def __a_sentence__(type_index, WORD_MIN, WORD_MAX):
    try:
        sentence = ''
        for i in range(random.randint(WORD_MIN, WORD_MAX)):
            type_item = word_types[type_index]
            data = type_item['data']
            sentence += data[random.randint(0, len(data) - 1)]
            type_index = __next_type__(type_item['type'])
    except Exception as err:
        pass
    finally:
        return sentence

def run(SENT_MIN, SENT_MAX, WORD_MIN, WORD_MAX):
    i = 1
    seq = []
    while (i <= random.randint(SENT_MIN, SENT_MAX)):
        start_type_index = random.randint(0, len(word_types) - 1)
        start_type = word_types[start_type_index]['type']
        if not start_type in ('quali', 'conj'):
            seq_item = __a_sentence__(start_type_index, WORD_MIN, WORD_MAX)
            if len(seq_item) > 0:
                seq.append(seq_item)
            i += 1
    return seq
