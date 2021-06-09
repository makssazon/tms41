import csv
import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader


def my_time(request):
    return HttpResponse(datetime.now())


def two_pow(request, number):
    return HttpResponse(f'2**{number} = {2 ** number}')


def my_word(request, word):
    if len(word) % 2:
        return redirect('time')
    else:
        return HttpResponse(f'{word[::2]}')


def add_user(request):
    if not os.path.exists('django_04_users.csv'):
        with open('django_04_users.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = ['first name', 'last name', 'age']
            csvwriter.writerow(fields)
    if request.method == 'POST':
        user = [request.POST.get('firstname'), request.POST.get('lastname'), request.POST.get('age')]
        with open('django_04_users.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(user)
        return HttpResponse(f"user {user[0]} {user[1]} {user[2]} added to file")


def form(request):
    if not os.path.exists('django_05_users.csv'):
        with open('django_05_users.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = ['first name', 'last name', 'age']
            csvwriter.writerow(fields)
    if request.method == 'POST':
        user = [request.POST.get('firstname'), request.POST.get('lastname'), request.POST.get('age')]
        with open('django_05_users.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(user)
        return HttpResponse(f"user {user[0]} {user[1]} {user[2]} added to file")
    if request.method == 'GET':
        template = loader.get_template('django_05.html')
        response = template.render({}, request)
        return HttpResponse(response)


def full_form(request):
    if request.method == 'POST':
        context = {'user': {'firstname': request.POST.get('firstname'),
                            'lastname': request.POST.get('lastname'),
                            'age': request.POST.get('age')}}
        return render(request, 'django_06_display.html', context)
    if request.method == 'GET':
        return render(request, 'django_06_form.html')
