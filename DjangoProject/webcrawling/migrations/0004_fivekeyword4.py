# Generated by Django 3.2.5 on 2021-11-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawling', '0003_fivekeyword3'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiveKeyword4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('five_keyword', models.CharField(max_length=50)),
                ('five_keyword1', models.CharField(max_length=10)),
                ('five_keyword2', models.CharField(max_length=10)),
                ('five_keyword3', models.CharField(max_length=10)),
                ('five_keyword4', models.CharField(max_length=10)),
                ('five_keyword5', models.CharField(max_length=10)),
            ],
        ),
    ]
