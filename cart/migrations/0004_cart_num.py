# Generated by Django 4.1.3 on 2022-12-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]