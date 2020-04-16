from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from .models import List2
from .forms import ListForm2
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

	if request.method == 'POST': 
			
			form = ListForm(request.POST or None)

			year = request.POST.get('endereco', None)

			if form.is_valid():
				form.save()
				all_items = List.objects.all
				messages.success(request, year)
				return render(request, 'home.html', {'all_items': all_items})

	else:	
	 		all_items = List.objects.all
	 		return render(request, 'home.html', {'all_items': all_items})



def sobre(request):
	my_name = "SampaAjuda"
	return render(request, 'sobre.html', {'name': my_name})

def faq(request):
	my_name = "SampaAjuda"
	return render(request, 'faq.html', {'name': my_name})	

def como_funciona(request):
	my_name = "SampaAjuda"
	return render(request, 'como_funciona.html', {'name': my_name})

def vrnm(request):
	nro_voluntarios = List.objects.all().count()
	nro_grupo_de_risco = List2.objects.all().count()

	return render(request, 'vrnm.html', {'nro_voluntarios': nro_voluntarios,'nro_grupo_de_risco': nro_grupo_de_risco})


def cadastro(request):

		if request.method == 'POST': 
			
			form = ListForm(request.POST or None)

			#year = request.POST.get('endereco', None)

			nro_whatsapp_form = request.POST.get('nro_whatsapp', None)

			all_whatsapps = List.objects.all().values_list('nro_whatsapp', flat=True) 
			all_items = List.objects.all

			for things in all_whatsapps:
			 	if things == str(nro_whatsapp_form):
			 		messages.success(request, 'Numero de Whatsapp ja esta cadastrado. Por favor tente outro numero.')
			 		return render(request, 'cadastro.html', {'all_items': all_items})

			if form.is_valid():
				form.save()
				all_items = List.objects.all
				messages.success(request, 'Cadastro realizado com sucesso. A SampAjuda conectara voce assim que tiver uma pessoa procurando ajuda próximo ao seu local e com as preferencias indicadas.')
				return render(request, 'cadastro.html', {'all_items': all_items})
		else:
	 		all_items = List.objects.all
	 		return render(request, 'cadastro.html', {'all_items': all_items})


def cadastro_gr(request):

		if request.method == 'POST': 
			
			form = ListForm2(request.POST or None)

			#year = request.POST.get('endereco', None)
			nro_whatsapp_form = request.POST.get('nro_whatsapp', None)

			all_whatsapps = List.objects.all().values_list('nro_whatsapp', flat=True) 
			all_items = List.objects.all

			for things in all_whatsapps:
			 	if things == str(nro_whatsapp_form):
			 		messages.success(request, 'Numero de Whatsapp ja esta cadastrado. Por favor tente outro numero.')
			 		return render(request, 'cadastro.html', {'all_items': all_items})

			if form.is_valid():
				form.save()
				all_items = List.objects.all
				messages.success(request, 'Cadastro realizado com sucesso. A SampAjuda entrara em contato assim que pudermos conectar voce com alguma pessoa que possa ajudar voce')
				return render(request, 'cadastro.html', {'all_items': all_items})

		else:
	 		all_items = List2.objects.all
	 		return render(request, 'cadastro_gr.html', {'all_items': all_items})

