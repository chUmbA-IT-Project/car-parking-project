from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import Notification


class Command(BaseCommand):
    help = 'Создает стартовые акции и бонусы для пользователей'

    def handle(self, *args, **options):
        # Акции для компании
        promos = [
            {
                'title': 'Скидка 10% на консультацию',
                'message': 'Первая консультация — со скидкой 10%. Успейте забронировать удобное для вас время!',
                'notification_type': 'promo',
            },
            {
                'title': 'Пакет "Семейный выбор"',
                'message': 'При consulировании 2 автомобилей для семьи — подробный сравнительный анализ в подарок.',
                'notification_type': 'promo',
            },
            {
                'title': 'Бесплатный отчет по Toyota',
                'message': 'Получите бесплатный PDF-отчет по истории и особенностям любой модели Toyota.',
                'notification_type': 'info',
            },
        ]

        users = User.objects.all()

        created = 0
        for user in users:
            for promo in promos:
                Notification.objects.create(
                    user=user,
                    title=promo['title'],
                    message=promo['message'],
                    notification_type=promo['notification_type'],
                )
                created += 1

        # Бонус за регистрацию — только для пользователей без уведомлений
        bonus = {
            'title': 'Бонус за регистрацию',
            'message': 'Спасибо за регистрацию! Вы получили бесплатную экспресс-консультацию по модели Toyota.',
            'notification_type': 'bonus',
        }
        for user in users:
            Notification.objects.create(
                user=user,
                title=bonus['title'],
                message=bonus['message'],
                notification_type=bonus['notification_type'],
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Создано {created} уведомлений'))