# Generated by Django 2.1.3 on 2018-12-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0005_posts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Status',
            field=models.BooleanField(default=1),
        ),
    ]