# Generated by Django 4.1.3 on 2023-06-24 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0007_alter_utilisateur_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
