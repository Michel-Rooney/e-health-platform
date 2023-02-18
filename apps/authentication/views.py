from django.shortcuts import render, redirect, HttpResponse
from apps.authentication.utils import login_is_valid
from django.contrib import messages
from django.contrib import auth


def login(request):
    if request.method == 'GET':
        return render(request, 'loginto.html')
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
        