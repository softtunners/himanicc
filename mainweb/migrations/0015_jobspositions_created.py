# Generated by Django 4.0.4 on 2023-03-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0014_alter_skills_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobspositions',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]