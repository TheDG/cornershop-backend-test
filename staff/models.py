"""Staff related models --> Option selection."""

from django.db import models
from django.contrib.auth.models import User
from lunch_poll.models import Menu, Option


class Selection(models.Model):
    """User selection model."""
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    selected_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # SHould be normalized, but for simplicity using redundant data
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customization = models.TextField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['menu', 'selected_by'], name='just on selection per day')
        ]

    def __str__(self):
        return str(self.id)
