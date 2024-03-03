from django.shortcuts import render
from .models import Product, Lesson, Group
from django.utils import timezone
from rest_framework import generics
from .serializers import ProductSerializer


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    lessons = Lesson.objects.filter(product=product)
    groups = Group.objects.filter(product=product)
    return render(request, 'product_detail.html', {'product': product, 'lessons': lessons, 'groups': groups})


    if request.method == 'POST':
        if 'grant_access' in request.POST:
            product.grant_access(request.user)

    return render(request, 'product_detail.html', {'product': product, 'lessons': lessons, 'groups': groups})

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
