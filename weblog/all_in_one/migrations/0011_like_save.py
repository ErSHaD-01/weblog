# Generated by Django 5.0.7 on 2024-07-24 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_in_one', '0010_alter_comment_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_in_one.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_in_one.user')),
            ],
        ),
        migrations.CreateModel(
            name='save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_in_one.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_in_one.user')),
            ],
        ),
    ]