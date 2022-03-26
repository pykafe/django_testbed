from django.db import models

# Create your models here.

class Project(models.Model):
    """This represents a catalpa project"""

    class Meta:
        permissions = [
            ("project_approve", "Can approve projects"),
        ]

    name = models.CharField(
        max_length=64, unique=True, null=False, blank=False, 
        help_text="the name of the catlapa project")
    
    description = models.TextField(
        null=True, blank=True,
        help_text="Shart description of the project"
    )

    start_date = models.DateField(
        null=True, blank=True,
        help_text="The starting date of the project"
    )

    end_date = models.DateField(
        null=True, blank=True,
        help_text="The end date of the project"
    )

    def __str__(self):
        return self.name