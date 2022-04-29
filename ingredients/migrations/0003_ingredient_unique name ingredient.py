# Generated by Django 4.0.2 on 2022-04-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_category_unique user category'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name',), name='unique name ingredient'),
        ),
    ]