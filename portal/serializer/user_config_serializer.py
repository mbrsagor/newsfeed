from rest_framework import serializers
from portal.models import Country, Source, KeyWord, UserConfig


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id', 'name'
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id', 'name'
        )


class KeyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = (
            'id', 'name'
        )


class UserConfigSerializer(serializers.ModelSerializer):
    countries = CountrySerializer(read_only=True, many=True)
    sources = SourceSerializer(read_only=True, many=True)
    keywords = KeyWordSerializer(read_only=True, many=True)

    class Meta:
        model = UserConfig
        fields = (
            'id', 'user', 'countries', 'sources', 'keywords'
        )
