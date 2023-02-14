# Generated by Django 4.1.5 on 2023-02-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criado', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Aguardando', 'Aguardando'), ('Saiu para entrega', 'Saiu para entrega'), ('Entregue', 'Entregue')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('valor', models.FloatField(null=True)),
                ('categoria', models.CharField(choices=[('Salgada', 'Salgada'), ('Doce', 'Doce'), ('Especial', 'Especial')], max_length=200, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('data_criado', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]