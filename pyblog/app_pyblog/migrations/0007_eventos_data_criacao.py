# Generated by Django 3.0.8 on 2020-08-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pyblog', '0006_remove_eventos_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]