# Generated by Django 3.0.2 on 2020-01-23 20:11

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
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='', max_length=200)),
                ('option1', models.CharField(default='', max_length=50)),
                ('option2', models.CharField(default='', max_length=50)),
                ('option3', models.CharField(default='', max_length=50)),
                ('option4', models.CharField(default='', max_length=50)),
                ('answer', models.CharField(default='', max_length=50)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyzeapp.Quiz')),
            ],
        ),
    ]
