from django.shortcuts import render, redirect
from django.http import HttpResponse # test
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username          = request.POST.get('username')
        email             = request.POST.get('email')
        password          = request.POST.get('password')
        confirm_password  = request.POST.get('confirm_password')

        if (len(username.strip()) == 0) or (len(email.strip()) == 0) or (len(password.strip()) == 0) or (len(confirm_password.strip()) == 0):
            messages.add_message(request, constants.ERROR, "Nenhum campo pode ficar vazio")
            return redirect('register')
        
        if (len(password) < 6):
            messages.add_message(request, constants.ERROR, 'A senha deve conter no mínimo 6 caracteres')
            return redirect('register')
        
        if password != confirm_password:
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')
            return redirect('register')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe')
            return redirect('register')
        
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            
            user.save()
            messages.add_message(request, constants.ERROR, 'Usuário salvo com sucesso')
            return redirect('register')
        
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('register')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('login')
        
        auth.login(request, user)
        return redirect('/')
