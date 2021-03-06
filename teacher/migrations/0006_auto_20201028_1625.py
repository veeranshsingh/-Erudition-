# Generated by Django 3.1.1 on 2020-10-28 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_upload_video_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_video',
            name='detail',
            field=models.ForeignKey(default=87, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher_detail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload_video',
            name='grade',
            field=models.IntegerField(blank=True, default=78),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload_video',
            name='topic',
            field=models.CharField(max_length=100),
        ),
    ]
