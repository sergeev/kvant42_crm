from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portal'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('report/', views.report_all, name='report_all'),
    path('reports/<int:pk>', views.report_show, name='report_show'),

    path('staff/', views.staff_all, name='staff_all'),
    path('staffs/<int:pk>', views.staff_show, name='staff_show'),

    path('arrows/', views.arrow_all, name='arrows'),
    path('arrows/<int:pk>', views.arrow_show, name='context'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)