# Generated by Django 4.1.2 on 2022-10-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='freqCard',
            field=models.CharField(max_length=50),
        ),
    ]
