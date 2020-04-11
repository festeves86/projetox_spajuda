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
	 		#all_items = List.objects.all
	 		return render(request, 'home.html', {})


def about(request):
	my_name = "John Elder"
	return render(request, 'about.html', {'name': my_name})

def como_funciona(request):
	my_name = "John Elder"
	return render(request, 'como_funciona.html', {'name': my_name})


def cadastro(request):

		if request.method == 'POST': 
			
			form = ListForm(request.POST or None)

			#year = request.POST.get('endereco', None)

			if form.is_valid():
				form.save()
				all_items = List.objects.all
				messages.success(request, 'Cadastro realizado com sucesso. A SampAjuda entrara em contato assim que pudermos conectar voce com alguma pessoa que possa contar com sua ajuda')
				return render(request, 'cadastro.html', {'all_items': all_items})
		else:
	 		all_items = List.objects.all
	 		return render(request, 'cadastro.html', {'all_items': all_items})


def cadastro_gr(request):

		if request.method == 'POST': 
			
			form = ListForm2(request.POST or None)

			#year = request.POST.get('endereco', None)

			if form.is_valid():
				form.save()
				all_items = List2.objects.all
				messages.success(request, 'Cadastro realizado com sucesso. A SampAjuda entrara em contato assim que pudermos conectar voce com alguma pessoa que possa ajudar voce')
				return render(request, 'cadastro_gr.html', {'all_items': all_items})
		else:
	 		all_items = List2.objects.all
	 		return render(request, 'cadastro_gr.html', {'all_items': all_items})


def delete(request, list_id):
	item = List.objects.get(pk = list_id)
	item.delete()
	messages.success(request, ('Item has been deleted'))
	return redirect('home')
