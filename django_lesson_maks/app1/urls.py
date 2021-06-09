from django.contrib import admin
from django.urls import path, include

from app1.views import my_time, two_pow, my_word, add_user

urlpatterns = [
    path('', my_time, name='time'),
    path('two_pow/<int:number>', two_pow, name='two_pow'),
    path('my_word/<str:word>', my_word, name='my_word'),
    path('add_user', add_user, name='add_user'),

]
