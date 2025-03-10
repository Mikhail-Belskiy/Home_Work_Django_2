import csv

from django.core.management.base import BaseCommand
from djmoney.money import Money

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            # print(phones)

            for phone in phones:
                # TODO: Добавьте сохранение модели
                phone = Phone(
                    name = phone['name'],
                    price = int(phone['price']),
                    image = phone['image'],
                    release_date = phone['release_date'],
                    lte_exists = phone['lte_exists'].lower()=='true'
                )
                phone.save()


