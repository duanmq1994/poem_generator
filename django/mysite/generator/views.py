from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import WordType, Rules, Visitor
from .poem import run
from .helpers import update_ip

TITLE = '缱绻诗歌生成器'
SENT_LEN = 5
WORD_LEN = 5
# SEQS = []

# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    update_ip(request, 'web') # 根据ip统计访客数量
    return render(
        request,
        'index.html',
        {
            'title':TITLE,
            'year':datetime.now().year,
            'sent_len':SENT_LEN,
            'word_len':WORD_LEN,
            # 'seqs':seqs,
        },
    )

def MakePoem(request):
    if request.method == 'POST':
        sent_len = int(request.POST['sent_len'])
        word_len = int(request.POST['word_len'])
        seqs = run(sent_len, word_len)
        if not isinstance(seqs, list):
            return JsonResponse({'code':400, 'message':seqs})
        return JsonResponse({'code':200, 'message':seqs})

# Api接口
def GetPoemPub(request):
    if request.method == 'GET':
        update_ip(request, 'api') # 根据ip统计访客数量
        sent_len = int(request.GET['sent_len'])
        word_len = int(request.GET['word_len'])
        seqs = run(sent_len, word_len)
        if not isinstance(seqs, list):
            return JsonResponse({'code':400, 'message':seqs})
        return JsonResponse({'code':200, 'message':seqs})
