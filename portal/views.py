from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import PortalSettings


def index(request):
    portal_title = PortalSettings.portal_title
    portal_title_links = {'portal_title': portal_title}
    return render(request, 'portal/index.html', portal_title_links)
