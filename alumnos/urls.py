from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), 
    path('registro/', views.registro, name='registro'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),  # Define la vista home
    path('info/', views.info, name='info'),
    path('carrito/', views.carrito, name='carrito'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('alo/', views.alo, name='alo'),
    path('perfil/', views.perfil, name='perfil'),
    path('soporte/', views.soporte, name='soporte'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
