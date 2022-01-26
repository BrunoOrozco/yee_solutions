# Generated by Django 3.2.9 on 2022-01-11 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objetivos', '0002_auto_20220104_1702'),
        ('users', '0003_alter_vendedores_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('concepto', models.TextField(blank=True, null=True)),
                ('costo', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('factura', models.CharField(max_length=20)),
                ('importe_sin_iva', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('rfc', models.CharField(blank=True, max_length=13, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('iva', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('mes', models.CharField(blank=True, max_length=1, null=True)),
                ('tipo_documento', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('descuento', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_objetivo', to='objetivos.objetivocliente')),
                ('vendedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedor_user', to='users.vendedores')),
            ],
            options={
                'verbose_name': 'Venta',
                'db_table': 'Venta',
            },
        ),
    ]
