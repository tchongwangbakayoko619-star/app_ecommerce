from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from e_commerce_app.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    """Utilise par le UserViewSet standard (config/api_router.py)."""

    class Meta:
        model = User
        fields = ["id", "name", "email", "username", "phone", "role", "url"]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        }


class CustomRegisterSerializer(RegisterSerializer):
    """Ajoute le champ phone au formulaire d'inscription de dj-rest-auth."""

    phone = serializers.CharField(required=False, allow_blank=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["phone"] = self.validated_data.get("phone", "")
        return data

    def save(self, request):
        user = super().save(request)
        user.phone = self.cleaned_data.get("phone", "")
        user.role = User.Role.CLIENT
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer[User]):
    """Utilise par dj-rest-auth pour /api/auth/user/ apres inscription/login."""

    class Meta:
        model = User
        fields = ["pk", "username", "email", "name", "phone", "role"]
        read_only_fields = ["pk", "email", "role"]
