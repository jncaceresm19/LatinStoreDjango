# Generated by Django 4.1.2 on 2024-06-28 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_recepcion', models.DateField()),
                ('tallas_disponibles', models.CharField(blank=True, max_length=100, null=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha_pedido', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.producto')),
            ],
        ),
    ]
