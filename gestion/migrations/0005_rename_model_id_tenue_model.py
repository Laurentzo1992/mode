# Generated by Django 4.1.3 on 2022-11-14 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0004_rename_ville_id_client_ville"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tenue", old_name="model_id", new_name="model",
        ),
    ]
