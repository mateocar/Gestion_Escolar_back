# Generated by Django 4.2.15 on 2024-10-12 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qualification', models.DecimalField(decimal_places=2, max_digits=3)),
                ('evaluation_date', models.DateTimeField(null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]