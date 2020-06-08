from django.urls import path, re_path
from .views import inicio,usuariolist,formulario,ingresar,logeadoslist

urlpatterns = [
    #/inicio/
    path('usuarios/', inicio, name='inicio'),
    path('usuario/', usuariolist.as_view(), name='usuario_list'),
    path('logeo/', logeadoslist.as_view(), name='logueados_list'),
    #/inicio/545/
    #re_path(r'^user/(?P<user_id>[0-9]+)/$', views.help, name='help'),
    #Ingresar
    path('', formulario),
    path('ingresar/', ingresar),
    #path('pruba1/', views.login_lista.as_view()),
    ]
