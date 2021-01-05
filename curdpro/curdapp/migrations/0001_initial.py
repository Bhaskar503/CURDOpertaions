# Generated by Django 3.1.4 on 2020-12-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('section_name', models.CharField(max_length=30)),
                ('class_name', models.CharField(max_length=10)),
                ('school_name', models.CharField(max_length=50)),
                ('telugu_marks', models.IntegerField()),
                ('hindi_marks', models.IntegerField()),
                ('english_marks', models.IntegerField()),
                ('maths_marks', models.IntegerField()),
                ('science_marks', models.IntegerField()),
                ('social_marks', models.IntegerField()),
            ],
        ),
    ]
