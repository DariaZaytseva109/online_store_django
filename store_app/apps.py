"""Импортируем необходимые классы"""
from django.apps import AppConfig


class StoreAppConfig(AppConfig):
    """Конфиг приложения"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_app'
