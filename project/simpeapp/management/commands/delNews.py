from django.core.management.base import BaseCommand, CommandError
from .models import News


class Command(BaseCommand):
    help = 'Удаляет все новости категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = News.objects.get(name=options['category'])
            News.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(
                f'Succesfully deleted all news from category {category.name}'))
        except News.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {category.name}'))



