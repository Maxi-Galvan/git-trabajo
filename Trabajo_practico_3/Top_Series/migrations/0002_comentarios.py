# Generated by Django 4.1.7 on 2023-04-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Top_Series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.TextField(max_length=50)),
                ('texto', models.TextField(max_length=500)),
            ],
        ),
    ]
