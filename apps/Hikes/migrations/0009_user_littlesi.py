# Generated by Django 2.2.3 on 2019-07-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hikes', '0008_auto_20190723_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='littleSi',
            field=models.IntegerField(default=0),
        ),
    ]
