# Generated by Django 3.1.1 on 2020-09-10 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('measures', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price_per_day', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
                ('category', models.CharField(blank=True, choices=[('TB', 'Tables'), ('CH', 'Chairs'), ('GZ', 'Arches & Gazebos'), ('TN', 'Tents'), ('TA', 'Tent Accessories'), ('ST', 'Stages'), ('PR', 'Projectors & Screens'), ('EF', 'Special Effects Equipments'), ('AU', 'Audio Systems'), ('LT', 'Lighting'), ('LN', 'Lenin'), ('HN', 'Hangers'), ('GL', 'Glasses & Stemware'), ('FO', 'Fun Food Equip'), ('FL', 'Floral Accessories'), ('CR', 'Floors & Carpet'), ('TR', 'Serving Trays'), ('WR', 'Flatware')], max_length=2, null=True)),
                ('color', models.CharField(blank=True, choices=[('BL', 'Black'), ('WH', 'White'), ('GY', 'Gray'), ('BR', 'Browns'), ('GR', 'Green'), ('BU', 'Blue'), ('PU', 'Purple'), ('RE', 'Red'), ('OR', 'Orange'), ('YE', 'Yellow')], max_length=2, null=True)),
                ('theme', models.CharField(blank=True, choices=[('NE', 'Neon'), ('BW', 'Black & White'), ('CR', 'Carnival'), ('DS', 'Disco'), ('SR', 'Soirées'), ('CK', 'Cocktail'), ('SH', 'Showers'), ('PP', 'Pool Parties'), ('FR', 'Farewell'), ('OD', 'Outdoor'), ('FN', 'Fancy')], max_length=2, null=True)),
            ],
        ),
    ]
