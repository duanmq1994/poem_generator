import random
from .models import WordType, Rules, Words
from django.shortcuts import get_object_or_404

def __a_sentence__(seq, end_rule, next_type, word_types, word_len):
    sentence = ''
    i = 1
    round_word_len = random.randint(1, word_len)
    while  i <= round_word_len:
        # 结尾
        if next_type == 'end':
            break
        # 不可用于结尾
        if i == round_word_len and next_type in end_rule:
            i -= 1

        wt_obj = WordType.objects.get(type_name=next_type)
        word_set = wt_obj.words_set.all()
        new_word = random.choice(word_set).word

        # 已选取的不重复使用
        if not new_word in seq:
            sentence += new_word
            after_types = wt_obj.after.split(', ')
            next_type = random.choice(after_types)
            i += 1
    return sentence

def run(sent_len, word_len):
    try:
        i = 1
        seq = ''
        
        word_types = WordType.objects.all().values()    
        start_rule = Rules.objects.get(rule_type='start').members.split(', ')
        end_rule = Rules.objects.get(rule_type='noend').members.split(', ')

        while i <= sent_len:
            start_type_index = random.randint(0, len(word_types)-1)
            start_type = word_types[start_type_index]['type_name']
            if start_type in start_rule:
                seq_item = __a_sentence__(seq, end_rule, start_type, word_types, word_len)
                if len(seq_item) > 0:
                    seq += seq_item
                    i += 1
                    seq += '/'
        return seq.split('/')
    except Exception as err:
        print(err)