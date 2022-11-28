from rest_framework import serializers

from .models import About, AboutBenefit, TeamAbout


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutBenefit
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamAbout
        fields = '__all__'
