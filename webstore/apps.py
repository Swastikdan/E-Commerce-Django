# The above class is a configuration class for a Django webstore application.
# The `StoreConfig` class is a Django app configuration class for the `webstore` app with a default
# auto field set to `BigAutoField`.
from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webstore'
