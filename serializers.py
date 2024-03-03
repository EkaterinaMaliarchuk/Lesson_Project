from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'start_time', 'cost', 'lesson_count']

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()
