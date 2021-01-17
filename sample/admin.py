from django.contrib import admin

from .models import Item


# 参考：Django 管理画面逆引きメモ
# https://qiita.com/zenwerk/items/044c149d93db097cdaf8

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', 'pos', 'tm', 'pts','trb','ast','stl','blk')

    class Meta:
        verbose_name = 'nba'
        verbose_name_plural = 'nba'
