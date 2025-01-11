from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

users = ['user1', 'user2', 'user3']


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
                info['form'] = UserRegister()
                return render(request, 'fifth_task/registration_page.html', info)
            if int(age) < 18:
                info['error'] = "Вы должны быть старше 18"
                info['form'] = UserRegister()
                return render(request, 'fifth_task/registration_page.html', info)
            if username in users:
                info['error'] = "Пользователь уже существует"
                info['form'] = UserRegister()
                return render(request, 'fifth_task/registration_page.html', info)

            info['form'] = form
            info['message'] = f'Приветствуем, {username}!'
    else:
        info['form'] = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {'custom_form': True}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username and password and repeat_password and age:
            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
                return render(request, 'fifth_task/registration_page.html', info)
            if int(age) < 18:
                info['error'] = "Вы должны быть старше 18"
                return render(request, 'fifth_task/registration_page.html', info)
            if username in users:
                info['error'] = "Пользователь уже существует"
                return render(request, 'fifth_task/registration_page.html', info)
        else:
            return render(request, 'fifth_task/registration_page.html', info)

        info['message'] = f'Приветствуем, {username}!'
    return render(request, 'fifth_task/registration_page.html', info)
