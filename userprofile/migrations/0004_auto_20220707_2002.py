# Generated by Django 3.2 on 2022-07-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20220706_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurseprofile',
            name='first_name',
            field=models.CharField(default='firstname', max_length=50),
        ),
        migrations.AddField(
            model_name='nurseprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='nurseprofile',
            name='last_name',
            field=models.CharField(default='lastname', max_length=50),
        ),
        migrations.AddField(
            model_name='nurseprofile',
            name='phone_number',
            field=models.CharField(default='12345678', max_length=10),
        ),
    ]