# Generated by Django 4.0.1 on 2022-01-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nftproject',
            name='mainImage',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/nftproject'),
        ),
    ]
