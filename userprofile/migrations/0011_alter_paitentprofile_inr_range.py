# Generated by Django 3.2 on 2022-07-13 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_auto_20220713_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paitentprofile',
            name='inr_range',
            field=models.CharField(default='', max_length=50),
        ),
    ]
