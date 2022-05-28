from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    """This represents a catalpa project"""

    class Meta:
        permissions = [
            ("approve_project", _("Can approve projects")),
        ]

    name = models.CharField(
        max_length=64, unique=True, null=False, blank=False,
        help_text=_("the name of the catlapa project"))

    description = models.TextField(
        null=True, blank=True,
        help_text=_("Short description of the project"),
    )

    start_date = models.DateField(
        null=True, blank=True,
        help_text=_("The starting date of the project"),
    )

    end_date = models.DateField(
        null=True, blank=True,
        help_text=_("The end date of the project"),
    )

    APPROVAL_UNAPPROVED= 'unapproved'
    APPROVAL_APPROVED = 'approved'
    APPROVAL_REJECTED = 'rejected'
    APPROVAL_CHOICES = (
        (APPROVAL_UNAPPROVED, _("Not Approved")),
        (APPROVAL_APPROVED, _("Approved")),
        (APPROVAL_REJECTED, _("Rejected")),
    )
    approval_status = models.CharField(
        max_length=16,
        choices = APPROVAL_CHOICES,
        default=APPROVAL_UNAPPROVED,
        help_text=_("The approval status of this project"),
    )

    def __str__(self):
        return self.name
