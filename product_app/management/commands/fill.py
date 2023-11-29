from django.core.management import BaseCommand

from product_app.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Удаляем все старые данные
        Category.objects.all().delete()
        category_list = [
            {'name': 'Пиломатериалы', 'description': 'доска обрезная и не обрезная, брус'},
            {'name': 'Для дома', 'description': 'Вещи для использования в домашнем обиходе'},
            {'name': 'Автотовары', 'description': 'Товары для автомобилей и мотоциклов'},
            {'name': 'Кухонная электроника', 'description': 'Холодильники, газовые плиты, духовые шкафы и.т.д.'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)
