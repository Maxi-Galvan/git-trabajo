# Generated by Django 4.1.7 on 2023-04-18 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Top_Series', '0003_proximas_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proximas_series',
            name='fecha_lanzamiento',
            field=models.DateField(),
        ),
    ]