# Generated by Django 2.0.7 on 2019-05-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190510_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opencv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='opencv/media')),
            ],
        ),
    ]