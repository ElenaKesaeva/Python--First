
"""
Migrations
"""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
    Migrations
    """

    dependencies = [
        ("services_salon", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.CharField(max_length=30)),
                ("time", models.CharField(max_length=20)),
                ("staff", models.TextField(blank=True)),
                ("description", models.TextField(blank=True)),
                (
                    "service",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services_salon.service",
                    ),
                ),
            ],
        ),
    ]
