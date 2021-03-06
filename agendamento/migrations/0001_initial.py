# Generated by Django 3.2.7 on 2021-09-24 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ubs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusAgendamento',
            fields=[
                ('id', models.AutoField(db_column='id_status_agendamento', primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('observacao', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'status_agendamentos',
                'db_table': 'status_agendamento',
            },
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(db_column='id_agendamento', primary_key=True, serialize=False)),
                ('minha_localizacao', models.CharField(max_length=255)),
                ('destino', models.CharField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agendamento.statusagendamento')),
                ('ubs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubs.ubs')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'agendamentos',
                'db_table': 'agendamento',
            },
        ),
    ]
