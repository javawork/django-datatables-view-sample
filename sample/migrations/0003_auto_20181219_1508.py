# Generated by Django 2.1.3 on 2018-12-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20181205_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '自治体データ', 'verbose_name_plural': '自治体データ'},
        ),
        migrations.AlterField(
            model_name='item',
            name='address',
            field=models.CharField(max_length=100, verbose_name='住所'),
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=6, verbose_name='自治体コード'),
        ),
        migrations.AlterField(
            model_name='item',
            name='furigana',
            field=models.CharField(max_length=30, verbose_name='ふりがな'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=15, verbose_name='市町村名'),
        ),
        migrations.AlterField(
            model_name='item',
            name='pref_name',
            field=models.CharField(max_length=4, verbose_name='県名'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tel',
            field=models.CharField(max_length=13, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='item',
            name='zipcode',
            field=models.CharField(max_length=8, verbose_name='郵便番号'),
        ),
    ]