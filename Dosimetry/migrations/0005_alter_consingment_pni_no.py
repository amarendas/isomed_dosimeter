# Generated by Django 4.2.5 on 2023-09-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dosimetry', '0004_alter_consingment_dispatch_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consingment',
            name='PNI_No',
            field=models.CharField(auto_created=True, max_length=10, primary_key=True, serialize=False, verbose_name='PNI No'),
        ),
    ]
