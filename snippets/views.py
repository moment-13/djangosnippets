from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return HttpResponse(b"Hello World")

def snippet_new(request):
    return HttpResponse('スニペットの登録')

def snippet_edit(request, snippet_id):
    return HttpResponse('スニペットの編集')




