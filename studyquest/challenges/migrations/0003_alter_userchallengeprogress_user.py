# Generated by Django 5.1.1 on 2024-09-21 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_alter_userchallengeprogress_user'),
        ('users', '0004_user_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchallengeprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenge_progress', to='users.user'),
        ),
    ]
