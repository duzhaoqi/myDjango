from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def detail(requset,question_id):
    return HttpResponse("将为您打开问卷 {}".format(question_id))

def results(request , question_id):
    response = "正在查看问卷 毛s 的结果 。"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("请为问卷 {} 提交你的答案".format(question_id))