"""
Migrations
"""
from django.db import migrations


class Migration(migrations.Migration):
    """
    Migration
    """

    dependencies = [
        ("services_salon", "0003_alter_servicedetails_service"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="servicedetails",
            options={"verbose_name_plural": "Service details"},
        ),
    ]
