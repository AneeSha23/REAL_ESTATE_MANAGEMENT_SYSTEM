# Generated by Django 4.1.5 on 2023-01-25 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_sellproperty_status_sellproperty_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproperty',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.customer'),
        ),
    ]
