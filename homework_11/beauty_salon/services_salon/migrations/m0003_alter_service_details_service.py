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
        ("services_salon", "0002_servicedetails"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicedetails",
            name="service",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="details",
                to="services_salon.service",
            ),
        ),
    ]
