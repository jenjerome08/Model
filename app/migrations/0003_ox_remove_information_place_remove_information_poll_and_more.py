# Generated by Django 5.0.6 on 2024-06-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_place_poll_site_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horn_length', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'oxen',
                'ordering': ['horn_length'],
            },
        ),
        migrations.RemoveField(
            model_name='information',
            name='place',
        ),
        migrations.RemoveField(
            model_name='information',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='information',
            name='sites',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='Information',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]