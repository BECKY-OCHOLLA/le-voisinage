# Generated by Django 3.1.3 on 2022-06-19 13:53

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_name', models.CharField(max_length=200)),
                ('hood_location', models.CharField(max_length=200)),
                ('hood_description', models.TextField(blank=True, max_length=500)),
                ('hood_photo', cloudinary.models.CloudinaryField(default='photo', max_length=255, verbose_name='photo')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNo', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('content', models.TextField(blank=True, max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('neighbourhood', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=250)),
                ('business_email', models.CharField(max_length=30)),
                ('business_desc', models.TextField(blank=True)),
                ('business_hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
