# Generated by Django 4.2.16 on 2024-09-21 17:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Página',
                'verbose_name_plural': 'Páginas',
                'ordering': ['order', 'title'],
            },
        ),
    ]
