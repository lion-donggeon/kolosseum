from django.db import models
from rest_framework import serializers
from .models import NftProject

class NftProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NftProject
        fields = '__all__'