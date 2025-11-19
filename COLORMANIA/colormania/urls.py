from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_colormania, name='index_colormania'),
    path('login-usuario/', views.login_usuario, name='login_usuario'),
    path('admin-login/', views.login_admin, name='login_admin'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('registro/', views.registro, name='registro'), 
    path('index_admin/', views.index_admin, name='admin_home'), 

    path('admin-pinturas/', views.admin_pinturas, name='admin_pinturas'),
    path('admin-productos/', views.admin_productos, name='admin_productos'),
    path('admin-selladores/', views.admin_selladores, name='admin_selladores'),
    path('admin-colores/', views.admin_colores, name='admin_colores'),
    path('admin-logout/', views.logout_admin, name='logout_admin'),
]