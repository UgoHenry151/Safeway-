# Generated by Django 4.0.4 on 2022-06-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, default='name', max_length=100, null=True),
        ),
    ]
