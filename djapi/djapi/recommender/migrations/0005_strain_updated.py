# Generated by Django 2.2.5 on 2019-09-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0004_auto_20190923_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
