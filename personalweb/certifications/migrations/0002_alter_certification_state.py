# Generated by Django 5.0.3 on 2024-04-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='state',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('done', 'Done')], default='in_course', max_length=20, verbose_name='State'),
        ),
    ]
