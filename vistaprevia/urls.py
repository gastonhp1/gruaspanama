from django.urls import path
from vistaprevia import views
from gruaspanama import views as gruasview

urlpatterns = [
    path('', views.index, name='index'),
    path('alquiler/', gruasview.alquiler, name="alquiler"),
    path('catalogo/', gruasview.catalogo, name="catalogo"),
]