# Generated by Django 3.1.7 on 2021-05-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='商品品牌')),
                ('shop_grossWeight', models.CharField(max_length=100, verbose_name='商品重量')),
                ('shop_id', models.CharField(max_length=50, verbose_name='商品id')),
                ('shop_name', models.CharField(max_length=50, verbose_name='商品标题')),
                ('shop_placeOfOrigin', models.CharField(max_length=50, verbose_name='商品发布地点')),
                ('shop_price', models.CharField(max_length=50, verbose_name='商品价格')),
            ],
        ),
        migrations.CreateModel(
            name='DiZhi',
            fields=[
            ],
            options={
                'verbose_name': '京东家电出货地分布统计',
                'verbose_name_plural': '京东家电出货地分布统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.data',),
        ),
        migrations.CreateModel(
            name='JiaQian',
            fields=[
            ],
            options={
                'verbose_name': '京东家电价钱数据区间统计',
                'verbose_name_plural': '京东家电价钱数据区间统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.data',),
        ),
        migrations.CreateModel(
            name='PinPai',
            fields=[
            ],
            options={
                'verbose_name': '京东家电品牌分布饼图',
                'verbose_name_plural': '京东家电品牌分布饼图',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.data',),
        ),
        migrations.CreateModel(
            name='PinpaiJiaZhi',
            fields=[
            ],
            options={
                'verbose_name': '京东家电品牌价值统计',
                'verbose_name_plural': '京东家电品牌价值统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.data',),
        ),
        migrations.CreateModel(
            name='ZhongLiang',
            fields=[
            ],
            options={
                'verbose_name': '京东家电重量大致分布统计',
                'verbose_name_plural': '京东家电重量大致分布统计',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.data',),
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name': '京东家电数据展示', 'verbose_name_plural': '京东家电数据展示'},
        ),
        migrations.AlterModelTable(
            name='data',
            table='app_data',
        ),
    ]