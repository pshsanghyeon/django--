# Generated by Django 4.1.3 on 2022-12-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_inarimenu_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
