from django.shortcuts import render

# Create your views here.

from drf_haystack.serializers import HaystackSerializer
from myapp.search_indexes import GoodsIndex
from rest_framework import serializers
from myapp.models import Goods

class GoodsSerializer(serializers.ModelSerializer):
    """
    序列化器
    """
    class Meta:
        model = Goods
        fields = ('id', 'name','price')

class GoodsIndexSerializer(HaystackSerializer):
    """
    Goods索引结果数据序列化器
    """
    object = GoodsSerializer(read_only=True)
    class Meta:
        index_classes = [GoodsIndex]
        fields = ('text', 'object')

from drf_haystack.viewsets import HaystackViewSet

class GoodsSearchViewSet(HaystackViewSet):
    index_models = [Goods]

    serializer_class = GoodsIndexSerializer
