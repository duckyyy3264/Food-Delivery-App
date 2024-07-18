# Generated by Django 3.2.7 on 2024-07-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20240715_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=7, null=True)),
                ('location', models.CharField(blank=True, max_length=300, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecuritySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_id', models.BooleanField(default=False)),
                ('touch_id', models.BooleanField(default=False)),
                ('pin_security', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.BooleanField(default=True)),
                ('dark_mode', models.BooleanField(default=False)),
                ('sound', models.BooleanField(default=False)),
                ('automatically_updated', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('ENGLISH', 'English'), ('Vietnamese', 'Vietnamese')], default='ENGLISH', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
