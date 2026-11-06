from django.http import HttpResponse

def index(request):
    return HttpResponse('Olá, Bem-vindo ao controlador de despesas pessoais.')