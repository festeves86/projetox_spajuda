from django.db import models

# Create your models here.

class List(models.Model):
	nome = models.CharField(max_length = 200, default='')
	item = models.CharField(max_length = 200, default='')
	sobrenome = models.CharField(max_length = 200, default='')
	nro_whatsapp = models.CharField(max_length = 200, default='', primary_key=True)
	email = models.CharField(max_length = 200, default='NA', blank=True, null=True)
	tipo_logradouro = models.CharField(max_length = 200, default='')
	endereco = models.CharField(max_length = 200, default='')
	complemento = models.CharField(max_length = 200, default='NA', blank=True, null=True)
	bairro = models.CharField(max_length = 200, default='')
	estado = models.CharField(max_length = 200, default='')
	cidade = models.CharField(max_length = 200, default='')
	CEP = models.CharField(max_length = 200, default='')
	compras_supermercados = models.BooleanField(default= False)
	compras_farmacia = models.BooleanField(default= False)
	passeio_pet = models.BooleanField(default= False)
	outras_ajudas = models.BooleanField(default= False)
	completed = models.BooleanField(default= False)
	radio_dist1 = models.BooleanField(default= False)
	radio_dist2 = models.BooleanField(default= False)
	radio_dist3 = models.BooleanField(default= False)
	radio_dist4 = models.BooleanField(default= False)
	conexao = models.CharField(max_length = 200, default='', blank=True, null=True)
	comentario1 = models.TextField(max_length = 200, default='', blank=True, null=True)
	comentario2 = models.TextField(max_length = 200, default='', blank=True, null=True)

	
	def __str__(self):
		chave_adm = self.bairro + self.nome  + self.sobrenome + self.cidade
		return chave_adm


class List2(models.Model):
	item = models.CharField(max_length = 200, default='')
	nome = models.CharField(max_length = 200, default='')
	sobrenome = models.CharField(max_length = 200, default='')
	nro_whatsapp = models.CharField(max_length = 200, default='',primary_key=True)
	email = models.CharField(max_length = 200, default='NA', blank=True, null=True)
	tipo_logradouro = models.CharField(max_length = 200, default='')
	endereco = models.CharField(max_length = 200, default='')
	complemento = models.CharField(max_length = 200, default='NA', blank=True, null=True)
	bairro = models.CharField(max_length = 200, default='')
	estado = models.CharField(max_length = 200, default='')
	cidade = models.CharField(max_length = 200, default='')
	CEP = models.CharField(max_length = 200, default='')
	compras_supermercados = models.BooleanField(default= False)
	compras_farmacia = models.BooleanField(default= False)
	passeio_pet = models.BooleanField(default= False)
	outras_ajudas = models.BooleanField(default= False)
	outras_ajudas_conteudo = models.TextField(max_length = 200, default='', blank=True, null=True)
	completed = models.BooleanField(default= False)
	conexao = models.CharField(max_length = 200, default='', blank=True, null=True)
	comentario1 = models.TextField(max_length = 200, default='', blank=True, null=True)
	comentario2 = models.TextField(max_length = 200, default='', blank=True, null=True)
	
	def __str__(self):
		chave_adm = self.bairro + self.nome  + self.sobrenome + self.cidade
		return chave_adm