# Generated by Django 3.1.1 on 2020-10-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201028_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]