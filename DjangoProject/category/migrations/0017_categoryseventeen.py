# Generated by Django 3.2.5 on 2021-11-01 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0016_categorysixteen'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorySeventeen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
