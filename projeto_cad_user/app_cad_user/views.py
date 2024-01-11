from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')
def usuarios(request):
    #Salvar os dados da tela para o banco de dados 
    novo_usuario = Usuario()
    novo_usuario.nome =  request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade') 
    novo_usuario.save()
    #exibir todos os usuaios ja cadastrados em nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #retornar os dados para a pagina
    return render (request,'usuarios/usuarios.html', usuarios )
