# Generated by Django 4.1.2 on 2023-01-25 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("AppEpic", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="contract",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="AppEpic.contract",
            ),
        ),
    ]
