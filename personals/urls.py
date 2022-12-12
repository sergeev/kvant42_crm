from django.urls import path

from . import views

app_name = 'personals'
urlpatterns = [
    path('', views.personals, name="personals"),
    path('personals-list/<str:pk', views.personals, name="personals"),
]