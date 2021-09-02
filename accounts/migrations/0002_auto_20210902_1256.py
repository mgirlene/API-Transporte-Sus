# Generated by Django 3.1.5 on 2021-09-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubs', '0002_auto_20210902_1256'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuario',
            name='cidade',
            field=models.ForeignKey(db_column='id_cidade', on_delete=django.db.models.deletion.DO_NOTHING, to='ubs.cidade'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='membro'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='ubs',
            field=models.ForeignKey(db_column='id_ubs', on_delete=django.db.models.deletion.DO_NOTHING, to='ubs.ubs'),
        ),
    ]