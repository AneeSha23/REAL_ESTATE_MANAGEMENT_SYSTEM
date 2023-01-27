# Generated by Django 4.1.5 on 2023-01-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_sellproperty_baths_sellproperty_bed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproperty',
            name='baths',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='sellproperty',
            name='bed',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=3, null=True),
        ),
    ]