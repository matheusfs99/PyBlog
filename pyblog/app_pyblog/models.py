from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publicacao(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(verbose_name='Data da Publicação', auto_now=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    imagem = models.ImageField(upload_to='imagem_publicacao/', blank=True, null=True)
    texto = models.TextField()

    class Meta:
        db_table = 'tbl_publicacao'

class Comentarios(models.Model):
    comentario = models.CharField(max_length=300, blank=True, null=True)
    data_comentario = models.DateTimeField(verbose_name='Data do Comentário', auto_now=True)
    publicacao = models.ForeignKey(Publicacao, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_comentarios'