# Generated by Django 4.1.3 on 2022-12-31 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_delete_menu_mainmenu_kind'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicmenu',
            name='kind',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='coffeemenu',
            name='kind',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='drinkmenu',
            name='kind',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='inarimenu',
            name='kind',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='setmenu',
            name='kind',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sidemenu',
            name='kind',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
