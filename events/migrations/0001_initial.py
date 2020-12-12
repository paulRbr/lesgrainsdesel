# Generated by Django 3.1.3 on 2020-12-08 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adherant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('picture', models.ImageField(default='images/default_icon.png', upload_to='images/users/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.CharField(max_length=300)),
                ('date_begin', models.DateTimeField(max_length=300)),
                ('date_end', models.DateTimeField(max_length=300)),
                ('icon', models.ImageField(default='/images/default_icon.png', upload_to='images/')),
                ('image', models.ImageField(default='/images/default_image.png', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adherant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.adherant')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
