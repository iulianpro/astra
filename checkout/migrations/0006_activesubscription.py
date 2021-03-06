# Generated by Django 3.1.2 on 2020-11-05 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0005_auto_20201024_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_email', models.CharField(blank=True, editable=False, max_length=32, null=True)),
                ('sub_date_created', models.CharField(blank=True, editable=False, max_length=32, null=True)),
                ('sub_period', models.IntegerField(blank=True, editable=False, null=True)),
                ('sub_date_start', models.CharField(blank=True, editable=False, max_length=32, null=True)),
                ('sub_date_end', models.CharField(blank=True, editable=False, max_length=32, null=True)),
                ('sub_price', models.IntegerField(blank=True, editable=False, null=True)),
                ('sub_currency', models.CharField(blank=True, editable=False, max_length=5, null=True)),
                ('sub_status', models.CharField(blank=True, editable=False, max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sub_customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
