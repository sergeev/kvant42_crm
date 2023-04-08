from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm
from students.models import StudentTeacherReport


def home(request):
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

    return render(request, 'home.html', {})


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


def report_show(request):
    if request.user.is_authenticated:
        report_show_l = StudentTeacherReport.objects.all()
        return render(request, 'report/reports.html', {'report_show_l': report_show_l})
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')


def report(request, pk):
    if request.user.is_authenticated:
        report_all = StudentTeacherReport.objects.get(id=pk)
        return render(request, 'report/report.html', {'report_all': report_all})
    else:
        messages.success(request, "Нужно войти в систему чтобы увидеть данные...")
        return redirect('portal:home')
