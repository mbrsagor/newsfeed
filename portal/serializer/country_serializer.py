from rest_framework import serializers
from portal.models import Country, UserConfig


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id', 'country_name'
        )


class UserConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfig
        fields = (
            'id', 'user', 'country'
        )
