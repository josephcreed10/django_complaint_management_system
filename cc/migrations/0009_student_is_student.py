# Generated by Django 4.1.3 on 2023-01-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0008_remove_complaint_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
