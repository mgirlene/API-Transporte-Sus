# Generated by Django 3.2.7 on 2021-09-09 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(db_column='id_cidade', primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'cidades',
                'db_table': 'cidade',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(db_column='id_estado', primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50, verbose_name='nome')),
                ('sigla', models.TextField(max_length=2, verbose_name='sigla')),
            ],
            options={
                'verbose_name_plural': 'estados',
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Ubs',
            fields=[
                ('id', models.AutoField(db_column='id_ubs', primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50)),
                ('endereco', models.CharField(max_length=255)),
                ('cnes', models.CharField(max_length=20)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubs.cidade')),
            ],
            options={
                'verbose_name_plural': 'ubs',
                'db_table': 'ubs',
            },
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(db_column='id_motorista', primary_key=True, serialize=False)),
                ('ubs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubs.ubs')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'motoristas',
                'db_table': 'motorista',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubs.estado'),
        ),
    ]
