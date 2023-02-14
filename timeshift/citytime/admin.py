from django.contrib import admin

from .models import City, TimeZone, Update


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('name', 'latitude', 'longitude', 'timezone')
    # Добавляем интерфейс для поиска по тексту постов
    # search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('name',)
    empty_value_display = 'empty'


@admin.register(TimeZone)
class TimeZoneAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('timezone_name', 'timezone_delta',)
    # Добавляем интерфейс для поиска по тексту постов
    # search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('timezone_name',)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('title', 'description', 'date',)
    # Добавляем интерфейс для поиска по тексту постов
    # search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('title',)
