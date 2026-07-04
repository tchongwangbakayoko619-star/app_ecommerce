from __future__ import annotations

import typing

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings

from e_commerce_app.users.models import User

if typing.TYPE_CHECKING:
    from allauth.socialaccount.models import SocialLogin
    from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest) -> bool:
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: SocialLogin) -> bool:
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def populate_user(
        self,
        request: HttpRequest,
        sociallogin: SocialLogin,
        data: dict[str, typing.Any],
    ) -> User:
        """Remplit le nom + fixe toujours le role a 'client' pour une connexion Google."""
        user = super().populate_user(request, sociallogin, data)
        if name := data.get("name"):
            user.name = name
        user.role = User.Role.CLIENT
        return user