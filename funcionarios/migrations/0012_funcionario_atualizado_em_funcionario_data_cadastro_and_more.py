# Generated by Django 4.0.4 on 2022-07-20 05:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0011_funcionario_funcionario_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='atualizado_em',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='data_cadastro',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='funcionario_code',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]