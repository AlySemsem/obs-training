# Generated by Django 4.1.7 on 2023-07-12 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_accountdata_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountData',
        ),
    ]
