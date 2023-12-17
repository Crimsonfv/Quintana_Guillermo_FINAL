# Generated by Django 4.2.7 on 2023-12-17 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('FechaDeInscripcionYHora', models.DateField()),
                ('Estado', models.CharField(max_length=50)),
                ('Observaciones', models.TextField(blank=True, null=True)),
                ('Institucion', models.ForeignKey(db_column='Institucion', on_delete=django.db.models.deletion.DO_NOTHING, to='Inscritos.instituciones')),
            ],
        ),
    ]
