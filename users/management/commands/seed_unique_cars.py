from django.core.management.base import BaseCommand
from users.models import Car, Notification
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Создаёт 26 уникальных автомобилей Toyota с разными параметрами'

    def handle(self, *args, **options):
        Car.objects.all().delete()

        cars_data = [
            # Land Cruiser 300 (3)
            {'brand': 'Toyota', 'model': 'Land Cruiser 300', 'year': 2024, 'price': 12500000, 'mileage': 0, 'engine': 3.5, 'power': 415, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'gasoline', 'color': 'Чёрный металлик', 'is_new': True, 'img': 'cars/toyota_landcruiser300_1.jpg'},
            {'brand': 'Toyota', 'model': 'Land Cruiser 300', 'year': 2023, 'price': 10900000, 'mileage': 15000, 'engine': 3.5, 'power': 415, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'gasoline', 'color': 'Белый перламутр', 'is_new': False, 'img': 'cars/toyota_landcruiser300_2.jpg'},
            {'brand': 'Toyota', 'model': 'Land Cruiser 300', 'year': 2022, 'price': 9500000, 'mileage': 45000, 'engine': 3.5, 'power': 415, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'gasoline', 'color': 'Серебристый', 'is_new': False, 'img': 'cars/toyota_landcruiser300_3.jpg'},
            # GR86 (2)
            {'brand': 'Toyota', 'model': 'GR86', 'year': 2024, 'price': 5200000, 'mileage': 0, 'engine': 2.4, 'power': 237, 'transmission': 'automatic', 'drive': 'rwd', 'fuel': 'gasoline', 'color': 'Красный', 'is_new': True, 'img': 'cars/toyota_gr86_1.jpg'},
            {'brand': 'Toyota', 'model': 'GR86', 'year': 2023, 'price': 4700000, 'mileage': 8000, 'engine': 2.4, 'power': 237, 'transmission': 'automatic', 'drive': 'rwd', 'fuel': 'gasoline', 'color': 'Синий', 'is_new': False, 'img': 'cars/toyota_gr86_2.jpg'},
            # Crown (2)
            {'brand': 'Toyota', 'model': 'Crown', 'year': 2024, 'price': 7800000, 'mileage': 0, 'engine': 2.4, 'power': 340, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'hybrid', 'color': 'Чёрный', 'is_new': True, 'img': 'cars/toyota_crown_1.jpg'},
            {'brand': 'Toyota', 'model': 'Crown', 'year': 2023, 'price': 6900000, 'mileage': 12000, 'engine': 2.4, 'power': 340, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'hybrid', 'color': 'Бронзовый', 'is_new': False, 'img': 'cars/toyota_crown_2.jpg'},
            # bZ3X (2)
            {'brand': 'Toyota', 'model': 'bZ3X', 'year': 2025, 'price': 6500000, 'mileage': 0, 'engine': 0.0, 'power': 245, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'electric', 'color': 'Голубой', 'is_new': True, 'img': 'cars/toyota_bz3x_1.jpg'},
            {'brand': 'Toyota', 'model': 'bZ3X', 'year': 2024, 'price': 5900000, 'mileage': 5000, 'engine': 0.0, 'power': 245, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'electric', 'color': 'Белый', 'is_new': False, 'img': 'cars/toyota_bz3x_2.jpg'},
            # Hilux (3)
            {'brand': 'Toyota', 'model': 'Hilux', 'year': 2024, 'price': 5800000, 'mileage': 0, 'engine': 2.8, 'power': 204, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'diesel', 'color': 'Серый', 'is_new': True, 'img': 'cars/toyota_hilux_1.jpg'},
            {'brand': 'Toyota', 'model': 'Hilux', 'year': 2023, 'price': 5100000, 'mileage': 20000, 'engine': 2.8, 'power': 204, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'diesel', 'color': 'Чёрный', 'is_new': False, 'img': 'cars/toyota_hilux_2.jpg'},
            {'brand': 'Toyota', 'model': 'Hilux', 'year': 2022, 'price': 4500000, 'mileage': 60000, 'engine': 2.8, 'power': 204, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'diesel', 'color': 'Белый', 'is_new': False, 'img': 'cars/toyota_hilux_3.jpg'},
            # RAV4 (3)
            {'brand': 'Toyota', 'model': 'RAV4', 'year': 2024, 'price': 4800000, 'mileage': 0, 'engine': 2.5, 'power': 222, 'transmission': 'variator', 'drive': 'awd', 'fuel': 'hybrid', 'color': 'Синий', 'is_new': True, 'img': 'cars/toyota_rav4_1.jpg'},
            {'brand': 'Toyota', 'model': 'RAV4', 'year': 2023, 'price': 4300000, 'mileage': 15000, 'engine': 2.5, 'power': 222, 'transmission': 'variator', 'drive': 'awd', 'fuel': 'hybrid', 'color': 'Серебристый', 'is_new': False, 'img': 'cars/toyota_rav4_2.jpg'},
            {'brand': 'Toyota', 'model': 'RAV4', 'year': 2023, 'price': 4100000, 'mileage': 25000, 'engine': 2.5, 'power': 222, 'transmission': 'variator', 'drive': 'awd', 'fuel': 'hybrid', 'color': 'Белый', 'is_new': False, 'img': 'cars/toyota_rav4_3.jpg'},
            # Raize (2)
            {'brand': 'Toyota', 'model': 'Raize', 'year': 2024, 'price': 2200000, 'mileage': 0, 'engine': 1.0, 'power': 98, 'transmission': 'variator', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Оранжевый', 'is_new': True, 'img': 'cars/toyota_raize_1.jpg'},
            {'brand': 'Toyota', 'model': 'Raize', 'year': 2023, 'price': 1900000, 'mileage': 10000, 'engine': 1.0, 'power': 98, 'transmission': 'variator', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Серебристый', 'is_new': False, 'img': 'cars/toyota_raize_2.jpg'},
            # Camry (3)
            {'brand': 'Toyota', 'model': 'Camry', 'year': 2024, 'price': 4500000, 'mileage': 0, 'engine': 2.5, 'power': 200, 'transmission': 'automatic', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Чёрный', 'is_new': True, 'img': 'cars/toyota_camry_1.jpg'},
            {'brand': 'Toyota', 'model': 'Camry', 'year': 2023, 'price': 3900000, 'mileage': 20000, 'engine': 2.5, 'power': 200, 'transmission': 'automatic', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Белый', 'is_new': False, 'img': 'cars/toyota_camry_2.jpg'},
            {'brand': 'Toyota', 'model': 'Camry', 'year': 2022, 'price': 3500000, 'mileage': 40000, 'engine': 2.5, 'power': 200, 'transmission': 'automatic', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Красный', 'is_new': False, 'img': 'cars/toyota_camry_3.jpg'},
            # Corolla (3)
            {'brand': 'Toyota', 'model': 'Corolla', 'year': 2024, 'price': 3200000, 'mileage': 0, 'engine': 1.6, 'power': 122, 'transmission': 'variator', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Серебристый', 'is_new': True, 'img': 'cars/toyota_corolla_1.jpg'},
            {'brand': 'Toyota', 'model': 'Corolla', 'year': 2023, 'price': 2800000, 'mileage': 15000, 'engine': 1.6, 'power': 122, 'transmission': 'variator', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Синий', 'is_new': False, 'img': 'cars/toyota_corolla_2.jpg'},
            {'brand': 'Toyota', 'model': 'Corolla', 'year': 2023, 'price': 2600000, 'mileage': 30000, 'engine': 1.6, 'power': 122, 'transmission': 'variator', 'drive': 'fwd', 'fuel': 'gasoline', 'color': 'Белый', 'is_new': False, 'img': 'cars/toyota_corolla_3.jpg'},
            # Fortuner (3)
            {'brand': 'Toyota', 'model': 'Fortuner', 'year': 2024, 'price': 6200000, 'mileage': 0, 'engine': 2.8, 'power': 204, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'diesel', 'color': 'Чёрный', 'is_new': True, 'img': 'cars/toyota_fortuner_1.jpg'},
            {'brand': 'Toyota', 'model': 'Fortuner', 'year': 2023, 'price': 5500000, 'mileage': 25000, 'engine': 2.8, 'power': 204, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'diesel', 'color': 'Белый', 'is_new': False, 'img': 'cars/toyota_fortuner_2.jpg'},
            {'brand': 'Toyota', 'model': 'Fortuner', 'year': 2022, 'price': 4800000, 'mileage': 50000, 'engine': 2.8, 'power': 204, 'transmission': 'automatic', 'drive': 'awd', 'fuel': 'diesel', 'color': 'Серый', 'is_new': False, 'img': 'cars/toyota_fortuner_3.jpg'},
        ]

        for c in cars_data:
            Car.objects.create(
                brand=c['brand'],
                model=c['model'],
                year=c['year'],
                price=c['price'],
                mileage=c['mileage'],
                engine_volume=c['engine'],
                power=c['power'],
                transmission=c['transmission'],
                drive=c['drive'],
                fuel=c['fuel'],
                color=c['color'],
                is_new=c.get('is_new', False),
                is_available=True,
                main_image=c['img'],
            )

        self.stdout.write(self.style.SUCCESS(f'Создано {Car.objects.count()} автомобилей с уникальными параметрами'))