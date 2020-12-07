from django.shortcuts import render, HttpResponse
from users.models import User

# Create your views here.


def register(request):
    """注册view视图函数"""
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)
        return HttpResponse("注册成功")
