from django.conf import settings
from django.db import models

from apps.common.models import TimeStampedModel

# Create your models here.
class Organization(TimeStampedModel):
    """
    Represents an organization that uses the transport platform,
    such as a school, college, tuition center, or company.
    """

    class OrganizationType(models.TextChoices):
        SCHOOL = "SCHOOL", "School"
        COLLEGE = "COLLEGE", "College"
        TUITION = "TUITION", "Tuition Center"
        COMPANY = "COMPANY", "Company"
        OTHER = "OTHER", "Other"

    name = models.CharField(max_length=255)
    organization_type = models.CharField(
        max_length=20,
        choices=OrganizationType.choices
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        blank=True,
    )
    address = models.TextField(
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "organizations"
        ordering = ["name"]

    def __str__(self):
        return self.name

class OrganizationMember(TimeStampedModel):
    """
    Represents a user's membership in an organization.
    """

    class Role(models.TextChoices):
        ORG_ADMIN = "ORG_ADMIN", "Organization Admin"
        DRIVER = "DRIVER", "Driver"
        MEMBER = "MEMBER", "Member"

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="members"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organization_memberships",
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "organization_members"
        ordering = ["organization", "user"]
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "user"],
                name="unique_organization_user",
            )
        ]


    def __str__(self):
        return f"{self.user} ({self.organization})"