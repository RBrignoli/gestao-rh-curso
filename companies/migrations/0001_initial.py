# Generated by Django 3.2.13 on 2022-05-04 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, verbose_name='Nome da MEI')),
                ('cnpj', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='CNPJ da MEI')),
                ('bank', models.CharField(max_length=256, verbose_name='Banco')),
                ('agency', models.CharField(max_length=32, verbose_name='Agência')),
                ('account_number', models.CharField(max_length=32, verbose_name='Conta')),
            ],
            options={
                'verbose_name': 'MEI',
                'verbose_name_plural': 'MEIs',
            },
        ),
    ]
