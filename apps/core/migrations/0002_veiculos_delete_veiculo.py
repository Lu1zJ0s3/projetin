# Generated by Django 5.0.2 on 2024-03-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='veiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=100)),
                ('fabricante', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='veiculo',
        ),
    ]
