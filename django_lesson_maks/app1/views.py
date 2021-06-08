from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def my_time(request):
    return HttpResponse(datetime.now())


def two_pow(request, number):
    return HttpResponse(f'2**{number} = {2 ** number}')
