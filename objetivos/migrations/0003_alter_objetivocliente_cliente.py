# Generated by Django 3.2.9 on 2022-01-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetivos', '0002_auto_20220104_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetivocliente',
            name='cliente',
            field=models.CharField(max_length=250),
        ),
    ]
