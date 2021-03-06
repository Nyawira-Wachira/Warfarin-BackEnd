# Generated by Django 3.2 on 2022-07-12 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inrrangeprofile',
            name='inr_type',
        ),
        migrations.AlterField(
            model_name='inrrangeprofile',
            name='remedy',
            field=models.CharField(default='EXtra Dose and or increase weekly dose by 10-20%', max_length=500),
        ),
        migrations.CreateModel(
            name='InrProtocolProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inr_protocal', models.CharField(default='', max_length=50)),
                ('inr_range', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inrprotocal_profile', to='userprofile.inrrangeprofile')),
            ],
            options={
                'db_table': 'inrprotocal_profile',
            },
        ),
    ]
