from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Publicacao(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(verbose_name='Data da Publicação', auto_now=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.CharField(max_length=300, blank=True, null=True, verbose_name='Descrição')
    imagem = models.ImageField(upload_to='imagem_publicacao/', blank=True, null=True)
    post = RichTextField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_publicacao'

class Comentarios(models.Model):
    comentario = models.CharField(max_length=300, blank=True, null=True)
    data_comentario = models.DateTimeField(verbose_name='Data do Comentário', auto_now=True)
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_comentarios'