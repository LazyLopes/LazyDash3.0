from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users

def login (request):
    print(request.method)
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'login.html', {'status': status})
    elif request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        
        # variavel de verificação se o usuário já existe
        user_exists = Users.objects.filter(login=login).exists()
        
        # se o usuário já existe, redireciona para a página de login com status de erro
        if user_exists:
            return redirect('/loginpage/login/?status=0')
        
        users = Users(
            login=login,
            senha=senha
        )
        users.save()
        
        return HttpResponse(f"Login: {login} | Senha: {senha}")
