# Generated by Django 4.0 on 2023-09-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytebender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfeedback', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
