# Generated by Django 3.2.5 on 2021-10-31 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_categoryfour'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
