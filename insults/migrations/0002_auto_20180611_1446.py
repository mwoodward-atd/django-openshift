# Generated by Django 2.0.6 on 2018-06-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insults', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word_type',
            field=models.CharField(choices=[('shortadj', 'Short Adjective'), ('longadj', 'Long Adjective'), ('noun', 'Noun')], max_length=20),
        ),
    ]