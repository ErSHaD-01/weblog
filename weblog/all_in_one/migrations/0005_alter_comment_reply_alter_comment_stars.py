# Generated by Django 5.0.7 on 2024-07-24 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_in_one', '0004_alter_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='all_in_one.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.IntegerField(),
        ),
    ]
