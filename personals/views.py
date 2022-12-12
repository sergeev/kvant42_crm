from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Staff
from django.db import models


def personals(request):
    projectsList = [{'id':'1',
    'name':'Онлайн-кинотеатр',
    'organization':'Кинотеатр с самой полной библиотекой фильмов.'},
    {'id':'2',
    'name':'Платформа с ИТ-курсами',
    'organization':'Курсы по фронтенду, бэкенду и мобильной разработке.'},
    {'id':'3',
    'name':'Рекрутинговый портал',
     'organization':'Вакансии для специалистов экстра-класса.'},
      ]
    return render(request, 'personal/personals.html', {'personals' :projectsList})


def project(request):
    return render(request, 'personal/single-personals.html')


def index(request):
    latest_staff_list = Staff.first_name
    context = {'latest_staff_list': latest_staff_list}
    return render(request, 'personal/index.html', context)


# def detail(request, account_id):
#     staff = get_object_or_404(Staff, pk=account_id)
#     return render(request, 'personal/detail.html', {'staff': staff})