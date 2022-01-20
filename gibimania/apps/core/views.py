from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from gibimania.apps.core.forms import RegisterForm, LoginForm


@login_required(login_url="login/")
def index(request):
    return render(request, 'index.html')


def registro(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(**data)
            return redirect('login')

        context['form'] = form

    return render(request, 'registro.html', context)


def do_login(request):
    context = dict()
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is not None:
                login(request, user)

                return redirect('index')

            form.add_error(None, "Credenciais incorretas")

        context['form'] = form

    return render(request, 'login.html', context)


@login_required(login_url="login/")
def curiosidades(request):
    return render(request, 'curiosidades.html')


@login_required(login_url="login/")
def turmajovem(request):
    return render(request, 'turmajovem.html')


@login_required(login_url="login/")
def turmacrianca(request):
    return render(request, 'turmacrianca.html')


def do_logout(request):
    logout(request)
    return redirect('login')