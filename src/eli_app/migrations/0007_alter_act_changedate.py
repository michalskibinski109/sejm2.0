# Generated by Django 5.0 on 2023-12-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "eli_app",
            "0006_remove_act_releasedby_remove_act_type_act_releasedby_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="act",
            name="changeDate",
            field=models.DateField(),
        ),
    ]
