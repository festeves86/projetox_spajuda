from django import forms
from .models import List
from .models import List2

class ListForm(forms.ModelForm):
	class Meta:
			model = List
			fields = ["item","nome","sobrenome","nro_whatsapp","email","tipo_logradouro","endereco","complemento","bairro","estado","cidade","CEP","compras_supermercados","compras_farmacia","passeio_pet","outras_ajudas","radio_dist1","radio_dist2","radio_dist3","radio_dist4","completed"]



class ListForm2(forms.ModelForm):
	class Meta:
			model = List2
			fields = ["item","nome","sobrenome","nro_whatsapp","email","tipo_logradouro","endereco","complemento","bairro","estado","cidade","CEP","compras_supermercados","compras_farmacia","passeio_pet","outras_ajudas","outras_ajudas_conteudo","completed"]