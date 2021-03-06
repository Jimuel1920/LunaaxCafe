# Generated by Django 4.0.2 on 2022-02-14 14:04

import backend.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_delete_meatproduct_alter_user_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_image', models.ImageField(default='profile_pic/image.jpg', upload_to=backend.models.image_path)),
                ('m_id', models.CharField(max_length=50, unique=True, verbose_name='Product id')),
                ('m_name', models.CharField(max_length=200, verbose_name='Product name')),
                ('m_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('m_size', models.CharField(max_length=200, verbose_name='Size')),
                ('m_cat', models.CharField(max_length=200, verbose_name='Catergory')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 14, 14, 4, 10, 453996, tzinfo=utc)),
        ),
    ]
