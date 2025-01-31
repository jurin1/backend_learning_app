# Generated by Django 5.1.5 on 2025-01-31 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255)),
                ('translation', models.CharField(max_length=255)),
                ('example', models.TextField(blank=True, null=True)),
                ('sentenceTranslation', models.TextField(blank=True, null=True)),
                ('mnemonic', models.TextField(blank=True, null=True)),
                ('oxford_list', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserWordProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('known', models.BooleanField(default=False)),
                ('lastLearned', models.IntegerField(default=0)),
                ('correctAnswersCount', models.IntegerField(default=0)),
                ('repetitionInterval', models.IntegerField(default=2)),
                ('lastCorrectAnswerDate', models.DateField(blank=True, null=True)),
                ('mnemonic', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.word')),
            ],
            options={
                'unique_together': {('user', 'word')},
            },
        ),
    ]
