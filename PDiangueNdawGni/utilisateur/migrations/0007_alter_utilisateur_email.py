# Generated by Django 4.1.3 on 2023-06-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0006_alter_utilisateur_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
    ]
