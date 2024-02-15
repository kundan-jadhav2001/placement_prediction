# Generated by Django 5.0 on 2024-02-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]