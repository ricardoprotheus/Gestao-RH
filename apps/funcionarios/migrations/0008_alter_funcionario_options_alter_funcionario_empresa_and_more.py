# Generated by Django 4.0.3 on 2022-03-04 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('funcionarios', '0007_funcionario_foto_funcionatio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'Funcionario', 'verbose_name_plural': 'Funcionarios'},
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
