# Generated by Django 2.1.3 on 2019-02-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0015_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Post_id',
            field=models.IntegerField(),
        ),
    ]
