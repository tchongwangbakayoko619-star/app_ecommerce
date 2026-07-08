from django.conf import settings
from django.shortcuts import redirect
from django.views import View


class ConfirmEmailRedirectView(View):
    """Redirige le lien de confirmation d'email vers le frontend (SPA)."""

    def get(self, request, key):
        return redirect(f"{settings.FRONTEND_URL}/confirm-email/{key}")


class EmailVerificationSentRedirectView(View):
    """Redirige vers une page frontend informant que l'email a ete envoye."""

    def get(self, request):
        return redirect(f"{settings.FRONTEND_URL}/email-verification-sent")
