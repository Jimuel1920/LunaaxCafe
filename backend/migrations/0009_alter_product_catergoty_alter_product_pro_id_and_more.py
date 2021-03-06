# Generated by Django 4.0.2 on 2022-02-14 10:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Catergoty',
            field=models.CharField(max_length=200, verbose_name='Catergory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='Product id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_name',
            field=models.CharField(max_length=200, verbose_name='Product name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_size',
            field=models.CharField(max_length=200, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 14, 10, 8, 20, 875251, tzinfo=utc)),
        ),
    ]
