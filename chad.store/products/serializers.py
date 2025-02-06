from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    descriprion = serializers.CharField()
    price = serializers.FloatField()
    currency = serializers.ChoiceField(choices = ['GEL', 'USD', 'EURO'])

class CartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)

class ProductTagSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    tag_name = serializers.CharField()