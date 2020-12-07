from django.urls import re_path
from hellowrld import views

urlpatterns = [
    re_path(r'^hello-world/$', views.first_views_func)
]