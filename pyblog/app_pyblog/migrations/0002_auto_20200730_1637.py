# Generated by Django 3.0.8 on 2020-07-30 19:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pyblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]