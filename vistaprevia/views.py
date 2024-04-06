from django.shortcuts import render

def index(request):
  params = {}
  params['nombre_sitio'] = 'Gruas Panamá - Inicio'
  return render(request, 'gruaspanama/index.html', params)


