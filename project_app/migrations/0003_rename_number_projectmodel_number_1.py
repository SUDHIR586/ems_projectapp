# Generated by Django 4.2.7 on 2023-12-31 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_alter_projectmodel_client_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmodel',
            old_name='number',
            new_name='number_1',
        ),
    ]
