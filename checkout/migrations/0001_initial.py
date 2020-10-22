# Generated by Django 3.1.2 on 2020-10-22 15:11

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('town_or_city', models.CharField(max_length=40)),
                ('app', models.CharField(choices=[('select', 'Selecteaza aplicatia'), ('smart_iptv', 'Smart IPTV'), ('set_iptv', 'Set IPTV'), ('net_iptv', 'Net IPTV'), ('iptv_extreme', 'IPTV Extreme'), ('mag_device', 'Dispozitiv MAG'), ('stb_device', 'Dispozitiv STB'), ('another_device', 'Alt dispozitiv')], default='select', max_length=40)),
                ('mac', models.CharField(max_length=40)),
                ('mac_pass', models.CharField(blank=True, max_length=40, null=True)),
                ('notes', models.CharField(blank=True, max_length=40, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]