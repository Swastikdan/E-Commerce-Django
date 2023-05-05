# The above class is a configuration class for a Django webstore application.
from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webstore'
