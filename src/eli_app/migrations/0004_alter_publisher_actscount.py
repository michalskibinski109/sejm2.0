# Generated by Django 5.0 on 2023-12-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eli_app", "0003_alter_actstatus_id_alter_documenttype_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publisher",
            name="actsCount",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
