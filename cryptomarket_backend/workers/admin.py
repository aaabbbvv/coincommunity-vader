from django.contrib import admin

from workers import models


class StatisticParserAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'is_calculated', 'is_calculating']
    ordering = ['-created_date']


class TempGitHubAdmin(admin.ModelAdmin):
    list_display = ['coin', 'value', 'time_type']
    readonly_fields = ['coin', 'value', 'time_type']
    list_filter = ['coin', 'time_type', ]
    ordering = ['coin']


class StatisticTempAdmin(admin.ModelAdmin):
    list_display = ['coin', 'value', 'time_type']
    readonly_fields = ['coin', 'value', 'time_type']
    ordering = ['coin']


class StatisticTempTrendingAdmin(admin.ModelAdmin):
    list_display = ['coin', 'value', 'time_type', 'ranking_type']
    readonly_fields = ['coin', 'value', 'time_type']
    ordering = ['coin']


class StatisticScrapersAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'created_date', 'coin', 'scrapper', 'status', 'updated_date']
    ordering = ['-created_date']
    list_filter = ['coin', 'scrapper', 'status']
    search_fields = ['task_id']


class TemGrowsValuesAdmin(admin.ModelAdmin):
    list_display = ['coin', 'value', 'time_type', 'ranking_type']
    readonly_fields = ['coin', 'value', 'time_type']
    list_filter = ['coin', 'time_type', 'ranking_type']
    ordering = ['coin']


admin.site.register(models.Coin)
admin.site.register(models.StatisticScrapper, StatisticScrapersAdmin)
admin.site.register(models.TempGrowthValues, TemGrowsValuesAdmin)
admin.site.register(models.TempTrendingValue, TemGrowsValuesAdmin)
admin.site.register(models.TempTotalValueByPeriod, TemGrowsValuesAdmin)
