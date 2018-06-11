# Generated by Django 2.0.6 on 2018-06-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('word_type', models.CharField(choices=[('shortadj', 'Short Adjective'), ('longadj', 'Long Adjective'), ('noun', 'noun')], max_length=20)),
            ],
            options={
                'ordering': ['word_type', 'word'],
            },
        ),
    ]
