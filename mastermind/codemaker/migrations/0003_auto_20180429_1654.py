# Generated by Django 2.0.4 on 2018-04-29 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codemaker', '0002_auto_20180429_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='created_at',
            new_name='createdAt',
        ),
    ]
