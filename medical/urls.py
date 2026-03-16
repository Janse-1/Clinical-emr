from django.urls import path
from . import views

#Rutas URL para seguir al archivo html correspondiente
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #Crud de pacientes
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:id>/', views.eliminar_paciente, name='eliminar_paciente'),
    #Expediente
    path("pacientes/<int:paciente_id>/expediente/",views.expediente_paciente, name="expediente_paciente"),
    path("expediente/ver/<int:expediente_id>/",views.ver_expediente,name="ver_expediente")
]