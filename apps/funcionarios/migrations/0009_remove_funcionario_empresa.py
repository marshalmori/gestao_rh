# Generated by Django 3.0 on 2019-12-19 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0008_funcionario_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='empresa',
        ),
    ]