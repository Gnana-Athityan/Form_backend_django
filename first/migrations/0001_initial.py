# Generated by Django 4.0.6 on 2022-07-31 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('know', models.TextField()),
                ('review', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
