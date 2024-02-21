from rest_framework import serializers
from .models import Sneaker

class SneakerSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id","owner","name","brand","description","created_at")
    model = Sneaker