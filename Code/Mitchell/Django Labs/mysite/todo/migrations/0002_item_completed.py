# Generated by Django 2.1.2 on 2018-10-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=False),
            preserve_default=False,
        ),
    ]
