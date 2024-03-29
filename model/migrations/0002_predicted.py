# Generated by Django 5.0.2 on 2024-02-25 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='predicted',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=10)),
                ('Stream', models.CharField(max_length=30)),
                ('NumberOfInternships', models.IntegerField()),
                ('CGPA', models.IntegerField()),
                ('Backlogs', models.IntegerField()),
                ('WebDevlopment', models.IntegerField()),
                ('DataScience', models.IntegerField()),
                ('GameDevlopment', models.IntegerField()),
                ('AndroidDevlopment', models.IntegerField()),
                ('GraphicsDesigner', models.IntegerField()),
                ('Prediction', models.CharField(max_length=10)),
            ],
        ),
    ]
