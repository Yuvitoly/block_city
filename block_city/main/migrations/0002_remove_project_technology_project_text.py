# Generated by Django 4.1.7 on 2023-03-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
        migrations.AddField(
            model_name='project',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
