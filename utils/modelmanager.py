from django.db.models.manager import Manager
from django.core.cache import cache

class CacheKey:
    pass

class ModelManager(Manager, CacheKey):
    cache = cache
