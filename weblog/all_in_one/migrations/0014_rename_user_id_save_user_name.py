# Generated by Django 5.0.7 on 2024-07-27 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_in_one', '0013_rename_status_post_is_published_category_parent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='save',
            old_name='user_id',
            new_name='user_name',
        ),
    ]