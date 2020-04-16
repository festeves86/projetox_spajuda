from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('sobre/',views.sobre, name='sobre'),
	path('vrnm/',views.vrnm, name='vrnm'),
	path('faq/',views.faq, name='faq'),
	path('quero_ajudar/',views.cadastro, name='quero_ajudar'),
	path('preciso_de_ajuda/',views.cadastro_gr, name='preciso_de_ajuda'),
    path('como_funciona/',views.como_funciona, name='como_funciona'),
]
