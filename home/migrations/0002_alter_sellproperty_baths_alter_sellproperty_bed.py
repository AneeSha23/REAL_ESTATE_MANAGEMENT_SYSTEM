# Generated by Django 4.1.5 on 2023-01-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproperty',
            name='baths',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sellproperty',
            name='bed',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
