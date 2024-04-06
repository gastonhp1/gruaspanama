from django.shortcuts import render


def catalogo(request):
  params = {}
  params['nombre_sitio'] = 'Gruas Panamá - Catalogo'
  return render(request, 'gruaspanama/catalogo.html', params)


def alquiler(request):
  params = {}
  params['nombre_sitio'] = 'Gruas Panamá - Alquiler'
  return render(request, 'gruaspanama/alquiler.html', params)
