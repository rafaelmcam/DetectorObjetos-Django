# Generated by Django 2.0.2 on 2019-05-10 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190510_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_featured',
            field=models.BooleanField(default=False),
        ),
    ]