# Generated by Django 4.0.4 on 2023-03-06 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0006_remove_userinfo_gid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userinfo',
        ),
    ]
