# Generated by Django 2.2.5 on 2019-11-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191106_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]