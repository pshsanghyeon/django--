# Generated by Django 4.1.3 on 2023-01-01 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_basicmenu_kind_coffeemenu_kind_inarimenu_kind_and_more'),
        ('cart', '0005_cart_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menu'),
        ),
    ]
