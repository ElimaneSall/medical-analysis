# Generated by Django 4.1.4 on 2022-12-21 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docteur', '0006_alter_analysemedicale_resultat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysemedicale',
            name='resultat',
            field=models.CharField(blank=True, default='Paludisme', max_length=200, null=True),
        ),
    ]
