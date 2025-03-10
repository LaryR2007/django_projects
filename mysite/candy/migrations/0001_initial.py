# Generated by Django 5.1.6 on 2025-03-10 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CandyDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.TextField()),
                ('flavor', models.CharField(max_length=100)),
                ('candy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='candy.candy')),
            ],
        ),
    ]
