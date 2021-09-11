from __future__ import annotations

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def is_prodil_admin(self, user: User):
        if user.is_active and user.has_perm("prodil.prodil_admin"):
            return True
        return False
