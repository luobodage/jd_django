from collections import Counter

import pandas
from django.contrib import admin
from .models import *
import numpy as np


# Register your models here.

# class DataAdmin(admin.ModelAdmin):
#     list_display = ('dog_title', 'salesLocation', 'dog_breed', 'dog_age', 'vaccineSituation', 'dog_price')
#     list_per_page = 15

class shop_dataAdmin(admin.ModelAdmin):
    list_display = ('shop_id', 'shop_name', 'shop_placeOfOrigin', 'brand', 'shop_price')
    list_per_page = 15

from django.contrib import admin

admin.AdminSite.site_header = '基于python爬虫的京东数据和分析系统'
admin.AdminSite.site_title = '京东数据分析系统'
# admin.site.register(Data, DataAdmin)
admin.site.register(shop_data, shop_dataAdmin)
data = pandas.read_csv("static/jd_data01.csv", encoding='utf-8')

# 把价格与重量改成改成浮点型
data['shop_grossWeight'] = data['shop_grossWeight'].astype('float')
data['shop_price'] = data['shop_price'].astype('float')

# 去空格
data['shop_name'] = data['shop_name'].str.replace(' ', '')


class JiaQianAdmin(admin.ModelAdmin):
    list_per_page = 1940

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )
        data_temp = data.groupby(pandas.cut(data['shop_price'], np.arange(0, 10000, 2000))).count()
        # 取每个区间的价格均值 并保留一位小数 把nan值变为0
        # 把宠物狗的价格分为0-10000 每2000元为一档进行分组 在这基础上 进行价格均值计算 并且输出
        data_temp1 = data.groupby(pandas.cut(data['shop_price'], np.arange(0, 10000, 2000))).mean().round(2)[
            'shop_price'].fillna(value=0)
        print(data_temp1)
        data_mean = list(data_temp1)
        print(data_mean)
        response.context_data['data_mean'] = data_mean
        data1 = []
        type = []
        for index, row in data_temp.iterrows():
            data1.append(row['shop_name'])
            type.append(str(index) + "元")
        response.context_data['type'] = type
        response.context_data['data1'] = data1
        print(type)
        print(data1)

        price1 = zip(type, data1)
        price = []
        for i in price1:
            list01 = list(i)
            price.append(list01)
        response.context_data['price'] = price

        return response


class PinPaiAdmin(admin.ModelAdmin):
    list_per_page = 1940

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )
        data_temps = data["brand"].tolist()
        res = dict(Counter(data_temps))
        res1 = sorted(res.items(), key=lambda item: item[1], reverse=True)[:10]

        print(res1)
        data1 = []
        leng = []
        # keys与values分别为该数据的键数组，值的数组。这里循环为字典添加对应键值
        for k, v in res1:
            data1.append({"value": v, "name": str(k)})
            leng.append(str(k))

        response.context_data['data1'] = data1
        response.context_data['leng'] = leng
        return response


class PinpaiJiaZhiAdmin(admin.ModelAdmin):
    list_per_page = 1940

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )
        data_temp = data.groupby(data['brand']).count()
        # 对宠物狗疫苗情况的价格进行平均值分析 可以看出两针疫苗和三针疫苗+狂犬疫苗的宠物狗价格均值较高
        data_mean01 = data.groupby(data['brand']).mean().round(1)[
            'shop_price'].fillna(value=0)
        data_mean = list(data_mean01)
        response.context_data['data_mean'] = data_mean
        data1 = []
        type = []
        for index, row in data_temp.iterrows():
            data1.append(row['shop_price'])
            type.append(str(index))
        response.context_data['type'] = type
        response.context_data['data1'] = data1
        return response


class ZhongLiangAdmin(admin.ModelAdmin):
    list_per_page = 1940

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )

        data_temp = data.groupby(pandas.cut(data['shop_price'], np.arange(0, 10000, 2000))).count()
        price_data1 = []
        price_type = []
        for index, row in data_temp.iterrows():
            price_data1.append(row['shop_name'])
            price_type.append(str(index) + "元")
        price1 = zip(price_type, price_data1)
        price = []
        for i in price1:
            list01 = list(i)
            price.append(list01)
        # 组合成[['(0, 1000]元', 842], ['(1000, 2000]元', 877], ['(2000, 3000]元', 170], ['(3000, 4000]元', 35], ['(4000,
        # 5000]元', 4], ['(5000, 6000]元', 4], ['(6000, 7000]元', 5], ['(7000, 8000]元', 3], ['(8000, 9000]元', 0]]

        response.context_data['price'] = price

        data_temp = data.groupby(data['shop_grossWeight']).count()
        data1 = []
        type = []

        for index, row in data_temp.iterrows():
            data1.append(row['brand'])
            type.append(str(index))
        response.context_data['type'] = type
        response.context_data['data1'] = data1
        age1 = zip(type, data1)
        # age = [[a, b] for a in type for b in data1]
        age = []
        for i in age1:
            list01 = list(i)
            age.append(list01)
        response.context_data['age'] = age
        return response


class DiZhiAdmin(admin.ModelAdmin):
    list_per_page = 1940

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )

        data_temp = data.groupby(data['shop_placeOfOrigin']).count()

        data_temp['brand'] = list(data_temp['brand'].sort_values(ascending=False))
        print(data_temp['brand'])
        print('------------')
        print(data_temp)

        data1 = []
        type = []
        for index, row in data_temp.iterrows():
            data1.append(row['brand'])
            type.append(str(index))
        # 分别把前十位价格数量传给网页前端
        response.context_data['type'] = type[:5]
        response.context_data['data1'] = data1[:5]
        return response


admin.site.register(JiaQian, JiaQianAdmin)
admin.site.register(PinPai, PinPaiAdmin)
admin.site.register(PinpaiJiaZhi, PinpaiJiaZhiAdmin)
admin.site.register(ZhongLiang, ZhongLiangAdmin)
admin.site.register(DiZhi, DiZhiAdmin)
