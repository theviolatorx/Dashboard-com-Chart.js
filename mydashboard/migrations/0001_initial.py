# Generated by Django 4.1.6 on 2023-02-02 00:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('data', models.DateTimeField(default=datetime.datetime(2023, 2, 1, 21, 26, 24, 580359))),
                ('nome_produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mydashboard.produto')),
                ('nome_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mydashboard.vendedor')),
            ],
        ),
    ]
