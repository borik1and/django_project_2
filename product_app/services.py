from django.core.cache import cache

from product_app.models import Category


def get_categories_cache():
    key = 'category_list'
    category_list = cache.get(key)
    if category_list is None:
        category_list = Category.objects.all()
        cache.set(key, category_list)
    return category_list
