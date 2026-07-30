from django.contrib import admin

from .models import Organization, OrganizationMember

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
       "name",
        "organization_type",
        "email",
        "phone_number",
        "is_active",
        "created_at", 
    )

    list_filter = (
        "organization_type",
        "is_active",
    )

    search_fields = (
        "name",
        "email",
        "phone_number",
    )

    ordering = ("name",)

@admin.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = (
        "organization",
        "user",
        "role",
        "is_active",
        "created_at",
    )

    list_filter = (
        "role",
        "is_active",
        "organization",
    )

    search_fields = (
        "user__username",
        "user__email",
        "organization__name",
    )

    ordering = (
        "organization",
        "user",
    )