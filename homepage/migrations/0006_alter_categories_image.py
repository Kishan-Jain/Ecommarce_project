# Generated by Django 5.0.4 on 2024-05-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_categories_image_alter_offer_nav_offer_disc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.FileField(blank=True, default=' ', null=True, upload_to='pics/categaries/'),
        ),
    ]
