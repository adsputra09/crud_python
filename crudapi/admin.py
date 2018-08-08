from django.contrib import admin
from .models import News,Topik

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    filter_horizontal = ('topik',)


admin.site.register(Topik)