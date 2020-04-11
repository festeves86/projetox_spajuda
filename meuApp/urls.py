from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('about/',views.about, name='about'),
	path('cadastro/',views.cadastro, name='cadastro'),
	path('cadastro_gr/',views.cadastro_gr, name='cadastro_gr'),
    path('como_funciona/',views.como_funciona, name='como_funciona'),
	path('delete/<list_id>', views.delete, name='delete'),
]
