"""djangocrud URL Configuration

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
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),




    # Urls de Jefe
    path('actualizarTrabajador/<int:id>/', views.actualizar_trabajador, name='actualizarTrabajador'),
    path('eliminarTrabajador/<int:id>/', views.eliminar_trabajador, name='eliminarTrabajador'),
    path('inicioJ/',views.inicioJefe, name='inicioJ'),
    path('listaTrabajadores/',views.listaTrabajadores, name='listaTrabajadores'),
    path('datoslaborales/',views.datoslaborales, name='datoslaborales'),


    #Urls de Personal
    path('inicioP',views.inicioPersonal, name='inicioP'),
    path('listaTrabajadoresP/',views.listaTrabajadoresP, name='listaTrabajadoresP'),
    path('crearTrabajador/', views.crear_trabajador, name='crearTrabajador'),
    path('actualizarTrabajadorP/<int:id>/', views.actualizar_trabajadorP, name='actualizarTrabajadorP'),










]
