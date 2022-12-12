from django.http import Http404
from django.shortcuts import render, get_object_or_404

from django.db import models


def index(request):
    return render(request, 'kvantums/index.html')
