# Generated by Django 5.1.2 on 2024-10-28 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_de_indicadores', '0008_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='indicador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicos', to='gestao_de_indicadores.indicador'),
        ),
    ]
