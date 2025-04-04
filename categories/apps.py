from django.apps import AppConfig
import algoliasearch_django as algoliasearch


class CategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categories'
    # def ready(self):
    #     # Import models here to avoid AppRegistryNotReady error
    #     from .models import Products, ProductIndex
        
    #     # Register with Algolia directly
    #     algoliasearch.register(Products, ProductIndex)
# categories/apps.py
# categories/apps.py

# import algoliasearch_django as algoliasearch
# from .models import Products, ProductIndex

# class CategoriesConfig(AppConfig):
#     name = 'categories'

#     def ready(self):
#         # Register the index only after all apps are loaded
#         from django.db.models import signals
#         from django.db import models
#         signals.post_migrate.connect(self.register_algolia_index, sender=self)

#     def register_algolia_index(self, sender, **kwargs):
#         # Ensure the index is registered after all apps have been loaded
#         algoliasearch.register(Products, ProductIndex)

