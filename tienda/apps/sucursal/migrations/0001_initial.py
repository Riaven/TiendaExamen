# Generated by Django 2.1.4 on 2018-12-10 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComuna', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTienda', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('encargado', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sucursal.Ciudad')),
                ('comuna', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sucursal.Comuna')),
            ],
        ),
    ]
