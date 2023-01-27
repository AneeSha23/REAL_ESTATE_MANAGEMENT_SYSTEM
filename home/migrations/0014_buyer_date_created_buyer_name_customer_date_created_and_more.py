# Generated by Django 4.1.5 on 2023-01-26 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_buyer_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sellproperty',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='EmiRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emiYear', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2, null=True)),
                ('emiAmount', models.CharField(choices=[('3000', '3000'), ('4000', '4000'), ('5000', '5000'), ('6000', '6000'), ('7000', '7000'), ('8000', '8000'), ('9000', '9000'), ('10000', '10000')], max_length=5, null=True)),
                ('bankName', models.CharField(max_length=100, null=True)),
                ('bankBranch', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.buyer')),
            ],
            options={
                'db_table': 'emirequest',
            },
        ),
    ]