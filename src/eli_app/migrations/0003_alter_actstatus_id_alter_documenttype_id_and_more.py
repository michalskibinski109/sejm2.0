# Generated by Django 5.0 on 2023-12-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eli_app", "0002_documenttype_act"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actstatus",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="documenttype",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="institution",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="keyword",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="reference",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
