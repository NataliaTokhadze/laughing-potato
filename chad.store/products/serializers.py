from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    descriprion = serializers.CharField()
    price = serializers.FloatField()
    currency = serializers.ChoiceField(choices = ['GEL', 'USD', 'EURO'])