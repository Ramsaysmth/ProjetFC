# Generated by Django 4.1.2 on 2022-10-16 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_hello_freqcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='freqCard',
            field=models.IntegerField(default=0),
        ),
    ]