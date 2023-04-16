from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .forms import SignUpForm
from students.models import StudentTeacherReport
from personals.models import Staff, Teacher
from kvantums.models import Kvantum
from .models import PortalSettings


def home(request):
    # Настройки сайта
    #portal_title = PortalSettings.get()
    # Проверка на вход в систему
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Авторизация
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы вошли в систему")
            return redirect('portal:home')
        else:
            messages.success(request, "Возника ошибка при входе систему")
            return redirect('portal:home')

    return render(request, 'home.html')


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect('portal:home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Вы удачно создали Ваш электронный профиль! Добро пожаловать!")
            return redirect('portal:home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def report_all(request):
    if request.user.is_authenticated:
        try:
            report_alls = StudentTeacherReport.objects.all()
            arrows = Kvantum.objects.all()
            context = {"report_alls": report_alls, "arrows": arrows}
            return render(request, "report/reports.html", context)
        except ObjectDoesNotExist:
            messages.success(request, "Нет данных в базе.")
            return render(request, "report/reports.html")
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')


def report_show(request, pk):
    if request.user.is_authenticated:
        try:
            report_status = StudentTeacherReport.objects.get(id=pk)
            context = {'report_status': report_status}
            return render(request, 'report/report.html', context)
        except ObjectDoesNotExist:
            messages.success(request, "Нет данных в базе.")
            return render(request, 'report/report.html', )
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')


def staff_all(request):
    if request.user.is_authenticated:
        try:
            staff_alls = Teacher.objects.all()
            return render(request, "staff/show.html", {"staff_alls": staff_alls})
        except ObjectDoesNotExist:
            messages.success(request, "Нет данных в базе.")
            return render(request, "staff/show.html")
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')


def staff_show(request, pk):
    if request.user.is_authenticated:
        try:
            teacher_personals = Teacher.objects.get(id=pk)
            staff_personals = Staff.objects.get(id=pk)
            return render(request, 'staff/personal.html', {'staff_personals': staff_personals, 'teacher_personals': teacher_personals })
        except ObjectDoesNotExist:
            messages.success(request, "Нет преподавателя в базе.")
            return render(request, 'staff/personal.html', )
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')


def arrow_all(request):
    if request.user.is_authenticated:
        try:
            arrows = Kvantum.objects.all()
            context = {'arrows': arrows}
            return render(request, 'arrows/arrows.html', context)
        except ObjectDoesNotExist:
            messages.success(request, "Нет направления в базе.")
            return render(request, 'arrows/arrows.html', )
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')


def arrow_show(request, pk):
    if request.user.is_authenticated:
        try:
            arrow_status = Kvantum.objects.get(id=pk)
            report_status = StudentTeacherReport.objects.get(id=pk)
            ok = arrow_status == report_status
            context = {'arrow_status': arrow_status, 'report_status': report_status, 'ok': ok}
            return render(request, 'arrows/show.html', context)
        except ObjectDoesNotExist:
            messages.success(request, "Нет данных в базе.")
            return render(request, 'arrows/show.html', )
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')

