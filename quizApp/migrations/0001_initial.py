# Generated by Django 3.2.9 on 2023-12-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=70)),
                ('q1', models.CharField(max_length=250)),
                ('o11', models.CharField(max_length=150)),
                ('o12', models.CharField(max_length=150)),
                ('o13', models.CharField(max_length=150)),
                ('o14', models.CharField(max_length=150)),
                ('a1', models.CharField(max_length=150)),
                ('q2', models.CharField(max_length=250)),
                ('o21', models.CharField(max_length=150)),
                ('o22', models.CharField(max_length=150)),
                ('o23', models.CharField(max_length=150)),
                ('o24', models.CharField(max_length=150)),
                ('a2', models.CharField(max_length=150)),
                ('q3', models.CharField(max_length=250)),
                ('o131', models.CharField(max_length=150)),
                ('o132', models.CharField(max_length=150)),
                ('o133', models.CharField(max_length=150)),
                ('o134', models.CharField(max_length=150)),
                ('a3', models.CharField(max_length=150)),
                ('q4', models.CharField(max_length=250)),
                ('o41', models.CharField(max_length=150)),
                ('o42', models.CharField(max_length=150)),
                ('o43', models.CharField(max_length=150)),
                ('o44', models.CharField(max_length=150)),
                ('a4', models.CharField(max_length=150)),
                ('q5', models.CharField(max_length=250)),
                ('o51', models.CharField(max_length=150)),
                ('o52', models.CharField(max_length=150)),
                ('o53', models.CharField(max_length=150)),
                ('o54', models.CharField(max_length=150)),
                ('a5', models.CharField(max_length=150)),
                ('q6', models.CharField(max_length=250)),
                ('o61', models.CharField(max_length=150)),
                ('o62', models.CharField(max_length=150)),
                ('o63', models.CharField(max_length=150)),
                ('o64', models.CharField(max_length=150)),
                ('a6', models.CharField(max_length=150)),
                ('q7', models.CharField(max_length=250)),
                ('o71', models.CharField(max_length=150)),
                ('o72', models.CharField(max_length=150)),
                ('o73', models.CharField(max_length=150)),
                ('o74', models.CharField(max_length=150)),
                ('a7', models.CharField(max_length=150)),
                ('q8', models.CharField(max_length=250)),
                ('o81', models.CharField(max_length=150)),
                ('o82', models.CharField(max_length=150)),
                ('o83', models.CharField(max_length=150)),
                ('o84', models.CharField(max_length=150)),
                ('a8', models.CharField(max_length=150)),
                ('q9', models.CharField(max_length=250)),
                ('o91', models.CharField(max_length=150)),
                ('o92', models.CharField(max_length=150)),
                ('o93', models.CharField(max_length=150)),
                ('o94', models.CharField(max_length=150)),
                ('a9', models.CharField(max_length=150)),
                ('q10', models.CharField(max_length=250)),
                ('o101', models.CharField(max_length=150)),
                ('o102', models.CharField(max_length=150)),
                ('o103', models.CharField(max_length=150)),
                ('o104', models.CharField(max_length=150)),
                ('a10', models.CharField(max_length=150)),
            ],
        ),
    ]