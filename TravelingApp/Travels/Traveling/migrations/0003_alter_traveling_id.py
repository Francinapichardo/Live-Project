# Generated by Django 4.1.5 on 2023-01-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Traveling', '0002_auto_20230112_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveling',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
