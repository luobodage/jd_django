from django.db import models


# Create your models here.


class shop_data(models.Model):
    brand = models.CharField(max_length=100, verbose_name='商品品牌')
    shop_grossWeight = models.CharField(max_length=100, verbose_name='商品重量')
    shop_id = models.CharField(max_length=50, verbose_name='商品id')
    shop_name = models.CharField(max_length=50, verbose_name='商品标题')
    shop_placeOfOrigin = models.CharField(max_length=50, verbose_name='商品发布地点')
    shop_price = models.CharField(max_length=50, verbose_name='商品价格')

    class Meta():
        db_table = "app_shop_data"
        verbose_name = "京东家电数据展示"
        verbose_name_plural = verbose_name


class Data(models.Model):
    dog_title = models.CharField(max_length=100, verbose_name='狗狗标题')
    salesLocation = models.CharField(max_length=100, verbose_name='售卖地址')
    dog_breed = models.CharField(max_length=50, verbose_name='狗狗品种')
    dog_age = models.CharField(max_length=50, verbose_name='狗狗年龄')
    vaccineSituation = models.CharField(max_length=50, verbose_name='疫苗情况')
    publisher = models.CharField(max_length=50, verbose_name='发布人')
    dog_price = models.CharField(max_length=20, verbose_name='狗狗价格')
    sellerPromise = models.CharField(max_length=200, verbose_name='卖家承诺')
    dog_detailedInterface = models.CharField(max_length=200, verbose_name='详情页面')




class JiaQian(Data):
    class Meta():
        proxy = True  # 使用代理
        verbose_name = "京东家电价钱数据区间统计"
        verbose_name_plural = verbose_name


class PinPai(Data):
    class Meta():
        proxy = True  # 使用代理
        verbose_name = "京东家电品牌分布饼图"
        verbose_name_plural = verbose_name


class PinpaiJiaZhi(Data):
    class Meta():
        proxy = True  # 使用代理
        verbose_name = "京东家电品牌价值统计"
        verbose_name_plural = verbose_name


class ZhongLiang(Data):
    class Meta():
        proxy = True
        verbose_name = "京东家电重量大致分布统计"
        verbose_name_plural = verbose_name


class DiZhi(Data):
    class Meta():
        proxy = True
        verbose_name = "京东家电出货地分布统计"
        verbose_name_plural = verbose_name
