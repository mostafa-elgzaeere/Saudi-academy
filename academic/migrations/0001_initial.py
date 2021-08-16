# Generated by Django 3.2 on 2021-05-02 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Perfect_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfect_students', to='academic.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfect_students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lectuer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('question', models.TextField(max_length=1000)),
                ('video', models.FileField(blank=True, null=True, upload_to='media/')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectuers', to='academic.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=400)),
                ('active', models.BooleanField(default=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('lectuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='academic.lectuer')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
