# Generated by Django 5.1.1 on 2024-10-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link')),
                ('status', models.CharField(choices=[('INPROGRESS', 'In progress'), ('FINISHED', 'Finished'), ('FREEZED', 'Freezed')], max_length=12, verbose_name='Status')),
            ],
        ),
    ]