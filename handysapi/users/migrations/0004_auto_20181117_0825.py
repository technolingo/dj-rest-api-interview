# Generated by Django 2.0.9 on 2018-11-17 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_membership_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_list_dummy', 'A dummy permission for listing objects'), ('can_view_dummy', 'A dummy permission for viewing objects'), ('can_edit_dummy', 'A dummy permission for editing objects'), ('can_delete_dummy', 'A dummy permission for deleting objects'))},
        ),
    ]