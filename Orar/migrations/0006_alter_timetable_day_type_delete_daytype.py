# Generated by Django 5.0.6 on 2024-07-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orar', '0005_rename_students_course_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day_type',
            field=models.CharField(choices=[('Odd', 'Odd Days'), ('Even', 'Even Days'), ('Any', 'Any Day')], max_length=4),
        ),
        migrations.DeleteModel(
            name='DayType',
        ),
    ]
