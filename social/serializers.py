from rest_framework import serializers
from .models import Dweet, Profile


class Profile(serializers.ModelSerializer):
    class Meta:
        madel = Profile
        fields = "__all__"


class DweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dweet
        fields = "__all__"