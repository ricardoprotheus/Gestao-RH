# Generated by Django 3.2.11 on 2022-01-20 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_alter_funcionario_user'),
        ('documentos', '0004_documento_proprietario_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='proprietario_documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]
