# Generated by Django 5.0.4 on 2024-05-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinder', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=100),
        ),
    ]
