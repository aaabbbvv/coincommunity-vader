from django.contrib import admin
from . import models


class RankingStatisticAdmin(admin.ModelAdmin):
    list_display = ['type', 'coin', 'total_week', 'total_month', 'total_three_month', 'growth_week', 'growth_month',
                    'total_six_month', 'total_year', 'trending_week', 'trending_month', 'total',
                    'trending_three_month', 'trending_six_month', 'trending_year']
    search_fields = ['type']
    list_filter = ['type', 'coin']


admin.site.register(models.RankingStatistic, RankingStatisticAdmin)
