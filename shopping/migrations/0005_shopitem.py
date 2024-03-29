# Generated by Django 3.2.8 on 2021-10-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shopping', '0004_delete_shopitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('shop_info', models.CharField(max_length=64)),
            ],
        ),
    ]
