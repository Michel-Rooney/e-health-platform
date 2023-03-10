from django.shortcuts import render, redirect, HttpResponse
from apps.authentication.utils import login_is_valid
from django.contrib.auth.models import User
from apps.platform_health.models import Person
from django.contrib import messages
from django.contrib import auth
from hashlib import sha256


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not login_is_valid(request, username, password):
            return redirect('/auth/login')
        
        user = auth.authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'Usuário ou senhas inválidas')
            return redirect('/auth/login')
        
        auth.login(request, user)
        messages.success(request, 'Usuário logado com sucesso')
        return HttpResponse(f'{username}, {password}')
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário saiu')
    return HttpResponse('saiu')

def register(request):
    if request.method == 'GET':
        return render(request, 'register')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        code = sha256(f'{username}{email}'.encode()).hexdigest()


        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            person = Person(user=user, code=code)
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('/')
        except:
            messages.error('Erro interno do sistema')
            return redirect('/auth/register')