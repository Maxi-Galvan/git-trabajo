"""MVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Top_Series.views import mostrar_contenido, cargar_serie, cargar_comentario, cargar_lanzamiento, Buscar_Serie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('root/', mostrar_contenido, name='mostrar-serie'),
    path('root/form/series', cargar_serie, name='cargar-serie'),
    path('root/form/comentarios', cargar_comentario, name='cargar-comentario'),
    path('root/form/prox_lanzamientos', cargar_lanzamiento, name='cargar-prox-lanzamiento'),
    path('root/form/search', Buscar_Serie.as_view(), name='Busqueda-Serie'),
]
