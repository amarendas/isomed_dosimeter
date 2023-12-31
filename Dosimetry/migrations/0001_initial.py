# Generated by Django 4.2.5 on 2023-09-27 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('createdOn', models.DateField(auto_created=True)),
                ('CustomerID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=15)),
                ('Address', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='Email: ')),
            ],
        ),
        migrations.CreateModel(
            name='Consingment',
            fields=[
                ('PNI_No', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='PNI No')),
                ('product', models.CharField(max_length=20, verbose_name='Product Name')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight of Container')),
                ('accepted', models.BooleanField(verbose_name=' Accepted or not')),
                ('No_of_boxes', models.IntegerField(max_length=3)),
                ('Arrival_date', models.DateField()),
                ('Dispatch_date', models.DateField(blank=True)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dosimetry.customer')),
            ],
        ),
    ]
