from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cadastrar/',views.cadastrar,name="cadastrar"),
    path("adicionar/",views.adicionar,name="adicionar"),
    path('apagar/<int:id>/',views.apagar,name="apagar"),
    path('editar/<int:id>/',views.editar,name="editar"),
    path('editar/atualizar/<int:id>/',views.atualizar,name="atualizar")
]