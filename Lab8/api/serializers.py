from rest_framework.serializers import ModelSerializer

from .models import Product,Category

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name', 'price', 'description', 'count', 'is_active'
        )
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name'
        )