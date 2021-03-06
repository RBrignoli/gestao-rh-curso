# Generated by Django 3.2.13 on 2022-05-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('motive', models.CharField(max_length=36)),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
