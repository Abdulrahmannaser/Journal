# Generated by Django 2.1.3 on 2018-12-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0006_auto_20181217_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Status',
            field=models.BooleanField(default='1'),
        ),
    ]
