from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ingreso/', views.ingreso_view, name='ingreso'),
    path('signup/', views.signup_view, name='signup'),
    path('citas-medicas/', views.citas_medicas, name='citas_medicas'),
    path('listar_citas/', views.listar_citas, name='listar_citas'),
    path('cancelar_cita/<int:cita_id>/', views.cancelar_cita, name='cancelar_cita'),
    path('tienda/', views.tienda, name='tienda'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('quitar_del_carrito/<int:producto_id>/', views.quitar_del_carrito, name='quitar_del_carrito'),
    path('realizar_compra/', views.realizar_compra, name='realizar_compra'),
    path('tips-cuidado/', views.tips_cuidado, name='tips_cuidado'),
]
