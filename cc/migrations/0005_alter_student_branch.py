# Generated by Django 4.1.3 on 2023-01-19 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0004_student_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(default='sELECT', on_delete=django.db.models.deletion.CASCADE, to='cc.branch'),
        ),
    ]
