# Generated by Django 4.0.4 on 2023-03-06 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0003_alter_userinfo_gid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailer.excel_file'),
        ),
    ]
