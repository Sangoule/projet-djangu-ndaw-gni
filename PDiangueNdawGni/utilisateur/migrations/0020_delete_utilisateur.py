# Generated by Django 4.1.3 on 2023-07-01 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0019_rename_iduser_userprofile_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]
