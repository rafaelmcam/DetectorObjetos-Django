# Generated by Django 2.0.7 on 2019-05-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]