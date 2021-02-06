# Generated by Django 3.1.4 on 2021-02-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210206_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='author',
        ),
        migrations.AddField(
            model_name='adherent',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='author_id',
            field=models.IntegerField(default=1),
        ),
    ]