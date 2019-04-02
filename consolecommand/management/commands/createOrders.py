from django.core.management.base import BaseCommand
from consolecommand import models
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    # Задаём текст помощи, который будет
    # отображён при выполнении команды
    # python manage.py createtags --help
    help = 'Creates specified number of tags'

    def add_arguments(self, parser):
        # Указываем сколько и каких аргументов принимает команда.
        # В данном случае, это один аргумент типа int.
        parser.add_argument('order_count', nargs=1, type=int)

    def handle(self, *args, **options):
        # Получаем аргумент, создаём необходимое количество тегов
        # и выводим сообщение об успешном завершении генерирования
        order_count = options['order_count'][0]

        for i in range(order_count):
            order = models.Order.objects.create(number = int(i),created_date = datetime(2018, 1, 1, 9, 0, 0) + timedelta(hours = int(i)))
            for j in range(random.randrange(1,5)):
                models.OrderItems.objects.create(order_id=order,product_name = 'Товар-{0}'.format(j),product_price = random.randrange(100,9999),amount=random.randrange(1,10))

        self.stdout.write('Successfully created {0} orders!'.format(order_count))