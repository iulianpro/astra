# Generated by Django 3.1.2 on 2020-10-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_app',
            field=models.CharField(choices=[('select', 'Selecteaza Aplicatia'), ('smart_iptv', 'Smart IPTV'), ('set_iptv', 'Set IPTV'), ('net_iptv', 'Net IPTV'), ('iptv_extreme', 'IPTV Extreme'), ('mag_device', 'Dispozitiv MAG'), ('stb_device', 'Dispozitiv STB')], default='select', max_length=40),
        ),
    ]