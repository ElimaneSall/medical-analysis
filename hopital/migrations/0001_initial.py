# Generated by Django 4.1.3 on 2022-11-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomService', models.CharField(default='', max_length=50)),
                ('chefService', models.CharField(default='', max_length=50)),
                ('adresse', models.CharField(default='', max_length=50)),
                ('nombreLit', models.CharField(default='', max_length=50)),
                ('nombreLitOccupe', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hopital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomHopital', models.CharField(default='', max_length=50)),
                ('adresse', models.CharField(default='', max_length=50)),
                ('telephone', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('logo', models.CharField(default='', max_length=50)),
                ('services', models.ManyToManyField(to='hopital.service', verbose_name='services_hopital')),
            ],
        ),
    ]
