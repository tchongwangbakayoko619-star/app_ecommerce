from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = "client", _("Client")
        ADMIN = "admin", _("Administrateur")

    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    phone = CharField(_("Telephone"), max_length=30, blank=True)
    role = CharField(
        _("Role"),
        max_length=10,
        choices=Role.choices,
        default=Role.CLIENT,
    )

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
