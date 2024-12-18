# Generated by Django 4.2 on 2024-11-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masomoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
