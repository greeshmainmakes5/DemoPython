# Generated by Django 3.2.4 on 2021-06-30 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='test', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
