"""
Admin
"""
from django.contrib import admin
from services_salon.models import Service, ServiceDetails


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    ServiceAdmin
    """
    def description_short(self, obj):
        """
        description
        :param obj:
        :return:
        """

        if len(obj.description) < 40:
            return obj.description
        return obj.description[:38] + "..."

    list_display = "pk", "name", "description_short"
    list_display_links = "pk", "name"


@admin.register(ServiceDetails)
class ServiceDetailsAdmin(admin.ModelAdmin):
    """
    ServiceDetails
    """
    list_display = "pk", "price", "time", "staff", "description"
