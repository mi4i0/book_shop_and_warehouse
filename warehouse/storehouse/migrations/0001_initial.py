# Generated by Django 3.1.7 on 2021-03-20 22:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('author', models.CharField(max_length=200, verbose_name='author')),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000, verbose_name='summary')),
                ('isbn', models.CharField(help_text='13 character ISBN number', max_length=13, verbose_name='ISBN')),
                ('language', models.CharField(max_length=20, verbose_name='language')),
                ('genre', models.CharField(max_length=200, verbose_name='genre')),
                ('price', models.CharField(help_text='Book price', max_length=20, verbose_name='price')),
            ],
            options={
                'ordering': ['title', 'author'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_order_id', models.IntegerField(help_text='Shop order id', verbose_name='shop order id')),
                ('customer_mail', models.EmailField(help_text='Customer e-mail address', max_length=254, verbose_name='customer mail')),
                ('order_date', models.CharField(max_length=20, verbose_name='order date')),
                ('shipped_date', models.DateField(help_text='Date when order moved to Done status', verbose_name='order date')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Waiting'), (2, 'In progress'), (3, 'Done')], default=1, help_text='Order status')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text='Books quantity', verbose_name='quantity')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storehouse.book')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storehouse.order')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'In stock'), (2, 'Reserved'), (3, 'Sold')], default=1, help_text='Book status')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storehouse.book')),
                ('order', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='storehouse.order')),
            ],
        ),
    ]