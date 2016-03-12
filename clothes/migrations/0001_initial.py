# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import clothes.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name=b'Nombre')),
                ('national', models.BooleanField(default=True, verbose_name=b'Marca nacional')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, verbose_name='G\xe9nero', choices=[(b'0', 'NI\xd1O'), (b'1', b'HOMBRE')])),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la Categor\xeda')),
            ],
            options={
                'verbose_name': 'Categor\xeda',
                'verbose_name_plural': 'Categor\xedas',
            },
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('available', models.BooleanField(default=True, verbose_name=b'Disponible')),
                ('description', models.TextField(verbose_name='Descripci\xf3n', blank=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'Nombre')),
                ('offer_price', models.PositiveSmallIntegerField(null=True, verbose_name=b'Precio de oferta (opcional)', blank=True)),
                ('price', models.PositiveSmallIntegerField(verbose_name=b'Precio')),
                ('slug', models.SlugField(editable=False)),
                ('stock', models.PositiveSmallIntegerField(verbose_name=b'Cantidad disponible')),
                ('brand', models.ForeignKey(verbose_name=b'Marca', to='clothes.Brand')),
                ('category', models.ForeignKey(verbose_name='Categor\xeda', to='clothes.Category')),
            ],
            options={
                'verbose_name': 'Prenda',
                'verbose_name_plural': 'Prendas',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', stdimage.models.StdImageField(upload_to=clothes.models.image_path, verbose_name=b'Imagen')),
                ('name', models.CharField(unique=True, max_length=30, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Im\xe1genes',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name=b'Talla')),
            ],
            options={
                'verbose_name': 'Talla',
                'verbose_name_plural': 'Tallas',
            },
        ),
        migrations.AddField(
            model_name='cloth',
            name='images',
            field=models.ManyToManyField(to='clothes.Image', verbose_name='Im\xe1genes de la prenda'),
        ),
        migrations.AddField(
            model_name='cloth',
            name='size',
            field=models.ManyToManyField(to='clothes.Size', verbose_name=b'Talla'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('name', 'gender')]),
        ),
    ]
