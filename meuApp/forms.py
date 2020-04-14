from django import forms
from .models import List
from .models import List2

class ListForm(forms.ModelForm):
	class Meta:
			model = List
			fields = ["item","nome","sobrenome","nro_whatsapp","email","tipo_logradouro","endereco","complemento","bairro","estado","cidade","CEP","compras_supermercados","compras_farmacia","passeio_pet","outras_ajudas","raio1","raio2","raio3","raio4"]



class ListForm2(forms.ModelForm):
	class Meta:
			model = List2
			fields = ["item","nome","sobrenome","nro_whatsapp","email","tipo_logradouro","endereco","complemento","bairro","estado","cidade","CEP","compras_supermercados","compras_farmacia","passeio_pet","outras_ajudas","outras_ajudas_conteudo"]