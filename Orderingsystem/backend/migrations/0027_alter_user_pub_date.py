# Generated by Django 4.0.2 on 2022-03-04 17:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_alter_product_pro_image_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 3, 4, 17, 35, 32, 975467, tzinfo=utc)),
        ),
    ]
