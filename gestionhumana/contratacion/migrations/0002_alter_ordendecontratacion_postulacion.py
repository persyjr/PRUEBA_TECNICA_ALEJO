# Generated by Django 5.2.3 on 2025-06-20 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecontratacion',
            name='postulacion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orden_contratacion', to='contratacion.postulacion'),
        ),
    ]
