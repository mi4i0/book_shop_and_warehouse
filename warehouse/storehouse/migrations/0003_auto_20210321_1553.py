# Generated by Django 3.1.7 on 2021-03-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0002_auto_20210320_2209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
        migrations.AlterField(
            model_name='order',
            name='shipped_date',
            field=models.DateField(help_text='Date when order moved to Done status', verbose_name='shipped date'),
        ),
    ]