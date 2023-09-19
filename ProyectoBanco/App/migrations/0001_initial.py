# Generated by Django 4.2.5 on 2023-09-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('tamaño', models.CharField(max_length=20)),
                ('resolucion', models.IntegerField()),
                ('categoria', models.CharField(max_length=15)),
                ('orientacion', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('duracion', models.CharField(max_length=5)),
                ('calidad', models.CharField(max_length=10)),
                ('categoria', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('categoria', models.CharField(max_length=15)),
                ('orientacion', models.CharField(max_length=10)),
                ('tipo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('tamaño', models.CharField(max_length=20)),
                ('resolucion', models.IntegerField()),
                ('categoria', models.CharField(max_length=15)),
                ('orientacion', models.CharField(max_length=10)),
            ],
        ),
    ]
