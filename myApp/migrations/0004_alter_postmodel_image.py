# Generated by Django 4.1.6 on 2023-03-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_postmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/image/'),
        ),
    ]
