#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : search_indexes.py
@version   : 1.0
@Time      : 2019/4/21 18:35
Description about this file:

"""

from haystack import indexes
# 修改此处，改成你自己的model
from myapp.models import Goods


# (Goods是子应用goods中的一个模型类)

# 修改此处，类名为模型类的名称+Index，比如模型类为Goods,则这里类名为GoodsIndex
class GoodsIndex(indexes.SearchIndex, indexes.Indexable):
    # 指明哪些字段产生索引，产生索引的字段，会作为前端检索查询的关键字；
    # document是指明text是使用的文档格式，产生字段的内容在文档中进行描述；
    # use_template是指明在模板中被声明需要产生索引；
    text = indexes.CharField(document=True, use_template=True)

    # 此外可以存在，可以不存在，看具体需要的数据
    """下面这些字段，在索引类中进行申明，在REST framework中，索引类的字段可以被作为索引查询结果返回数据额来源"""
    id = indexes.IntegerField(model_attr='id')
    name = indexes.CharField(model_attr='name')
    price = indexes.DecimalField(model_attr='price')

    """也就是说，前端在索引的时候，可以按照text=xxx,也可以按照id=xxx,name=xxx等，我们的数据返回也是返回id,name,price """

    # 修改此处，返回的是你自己的model
    def get_model(self):
        """获取模型类"""
        return Goods



    # 修改return 可以修改返回查询集的内容，比如返回时，有什么条件限制的时候
    def index_queryset(self, using=None):
        """声明满足索引要求的返回的查询集"""
        return Goods.objects.all()
