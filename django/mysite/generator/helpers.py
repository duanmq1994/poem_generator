from .models import Visitor, Words, WordType
from datetime import datetime
from django.shortcuts import get_object_or_404
from .readJson import read

def get_ip(request):
    client_ip = ''
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        client_ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0] # 真实IP
    else:
        client_ip = request.META['REMOTE_ADDR'] # 代理IP
    return client_ip

def update_ip(request, end_point):
    ip = get_ip(request)
    if len(ip) > 0:
        try:
            visitor = Visitor.objects.get(ip=ip, end_point=end_point)
            visitor.count += 1
            visitor.save()
        except:
            Visitor.objects.create(ip=ip, end_point=end_point, count=1)

def __insert_word__():
    types = read('./static/words.json')
    for t in types:
        t_id = WordType.objects.get(type_name=t['type']).id
        for w in t['data']:
            Words.objects.create(word=w, word_type_id=t_id)
