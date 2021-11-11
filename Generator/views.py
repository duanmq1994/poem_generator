"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, send_from_directory, request
from Generator import app
from Generator import generator
from Generator.helper import readJson, adminOpt
import os

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

SENT_LEN = 5
WORD_LEN = 5

JSON_PATH = '../json/words.json'
RULE_PATH = '../json/rules.json'
COUNT_PATH = '../json/counts'
WORD_TYPES = readJson.read(JSON_PATH)
RULES = readJson.read(RULE_PATH)
COUNTS = int(readJson.just_read(COUNT_PATH))

title = '缱绻诗歌生成器'
year = datetime.now().year

@app.route('/admin')
def admin():
    return render_template(
        'admin.html',
        title = 'admin',
        counts = COUNTS,
        year = year,
        word_types = WORD_TYPES,
        word_msg = {},
        delete_msg = {},
        type_msg = {}
    )

@app.route('/add_word', methods=['post'])
def add_word():
    word_msg = {}
    try:
        change_type = request.form.get('select')
        word = request.form.get('word_add')
        check = adminOpt.check_word(WORD_TYPES, word)
        if check != 'ok':
            raise Exception(check)
        if len(word) == 0:
            raise Exception('请添加词汇后再提交！')
        adminOpt.add_word(WORD_TYPES, JSON_PATH, change_type, word)
        word_msg['code'] = 'ok'
    except Exception as err:
        word_msg['code'] = 'error'
        word_msg['msg'] = err
        pass
    finally:
        return render_template(
            'admin.html',
            title = 'admin',
            counts = COUNTS,
            year = year,
            word_types = WORD_TYPES,
            word_msg = word_msg,
            type_msg = {},
            delete_msg = {}
        )

@app.route('/add_type', methods=['post'])
def add_type():
    type_msg = {}
    type_name = ''
    try:
        new_type = request.form.get('type_name')
        change_type = request.form.get('select_type')
        next_types = request.form.getlist('select_multi')
        start = request.form.get('start')
        end = request.form.get('end')

        if len(next_types) == 0 and end != 'on':
            raise Exception('“可接类型”或“可结尾”必须选一个！')
        if len(new_type) == 0:
            type_name = change_type
        else:
            type_name = new_type

        adminOpt.update_type(WORD_TYPES, JSON_PATH, type_name, next_types, end)
        adminOpt.update_start_rule(RULES, RULE_PATH, type_name, start)

        type_msg['code'] = 'ok'
    except Exception as err:
        type_msg['code'] = 'error'
        type_msg['msg'] = err
        pass
    finally:
        return render_template(
            'admin.html',
            title = 'admin',
            counts = COUNTS,
            year = year,
            word_types = WORD_TYPES,
            word_msg = {},
            delete_msg = {},
            type_msg = type_msg
        )

@app.route('/delete_type', methods=['post'])
def delete_type():
    delete_msg = {}
    try:
        type_name = request.form.get('delete_type')
        if len(type_name) == 0:
            raise Exception('请先选择一个类型！')
        adminOpt.delete_type(WORD_TYPES, JSON_PATH, RULES, RULE_PATH, type_name)
        delete_msg['code'] = 'ok'
    except Exception as err:
        delete_msg['code'] = 'error'
        delete_msg['msg'] = err
        pass
    finally:
        return render_template(
            'admin.html',
            title = 'admin',
            counts = COUNTS,
            year = year,
            word_types = WORD_TYPES,
            word_msg = {},
            type_msg = {},
            delete_msg = delete_msg
        )

@app.route('/')
@app.route('/home')
def home():
    now_count = COUNTS + 1
    readJson.just_write(COUNT_PATH, str(now_count))
    return render_template(
        'index.html',
        title = title,
        counts = now_count,
        year = year,
        seqs = [],
        sent_len = SENT_LEN,
        word_len = WORD_LEN
    )

@app.route('/custom', methods=['post'])
def custom():
    SENT_LEN = int(request.form.get('sent_len'))
    WORD_LEN = int(request.form.get('word_len'))

    seq_list = generator.run(WORD_TYPES, RULES, SENT_LEN, WORD_LEN)
    return render_template(
        'index.html',
        title = title,
        counts = COUNTS,
        year = year,
        seqs = seq_list,
        sent_len = SENT_LEN,
        word_len = WORD_LEN
    )