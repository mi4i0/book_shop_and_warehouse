# Generated by Django 3.1.7 on 2021-03-21 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0004_auto_20210321_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='order_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_order_item', to='storehouse.orderitem'),
        ),
    ]
