# Generated by Django 4.1.3 on 2022-11-26 23:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docteur', '0004_rename_qrccode_dossiermedical_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvousmedical',
            name='date_RV',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
