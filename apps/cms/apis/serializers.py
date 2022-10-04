from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ..models import *


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
