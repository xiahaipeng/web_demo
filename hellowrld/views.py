from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

def first_views_func(request):
    return HttpResponse("<h1>傻逼计金山</h1>")
# Create your views here.
