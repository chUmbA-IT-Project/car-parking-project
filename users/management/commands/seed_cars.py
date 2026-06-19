import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management.base import BaseCommand
from users.models import Car


class Command(BaseCommand):
    help = 'Заполняет базу данных автомобилями'

    def handle(self, *args, **kwargs):
        cars_data = [
            # Toyota Land Cruiser 300 (3 авто)
            {'brand': 'Toyota', 'model': 'Land Cruiser 300', 'year': 2024, 'price': 12000000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 3.3, 'power': 299, 'color': 'Черный', 'is_new': True, 'description': 'Флагманский внедорожник Toyota Land Cruiser 300 — это сочетание роскоши, комфорта и невероятных внедорожных возможностей. Оснащен мощным дизельным двигателем V6.'},
            {'brand': 'Toyota', 'model': 'Land Cruiser 300', 'year': 2024, 'price': 12500000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 3.3, 'power': 299, 'color': 'Белый', 'is_new': True, 'description': 'Премиальный внедорожник с улучшенной шумоизоляцией и системой Multi-Terrain Select.'},
            {'brand': 'Toyota', 'model': 'Land Cruiser 300', 'year': 2023, 'price': 11500000, 'mileage': 5000, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 3.3, 'power': 299, 'color': 'Серый', 'is_new': False, 'description': 'Внедорожник в отличном состоянии, полный привод, кожанный салон.'},
            
            # Toyota GR86 (2 авто)
            {'brand': 'Toyota', 'model': 'GR86', 'year': 2024, 'price': 4500000, 'mileage': 0, 'transmission': 'manual', 'drive': 'rear', 'fuel': 'gasoline', 'engine_volume': 2.4, 'power': 235, 'color': 'Красный', 'is_new': True, 'description': 'Спортивное купе Toyota GR86 — идеальный выбор для ценителей драйва.'},
            {'brand': 'Toyota', 'model': 'GR86', 'year': 2023, 'price': 4200000, 'mileage': 3000, 'transmission': 'manual', 'drive': 'rear', 'fuel': 'gasoline', 'engine_volume': 2.4, 'power': 235, 'color': 'Синий', 'is_new': False, 'description': 'Спорткар в идеальном состоянии, пробег 3000 км.'},
            
            # Toyota Crown (2 авто)
            {'brand': 'Toyota', 'model': 'Crown', 'year': 2024, 'price': 7000000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'rear', 'fuel': 'hybrid', 'engine_volume': 2.5, 'power': 249, 'color': 'Черный', 'is_new': True, 'description': 'Бизнес-седан Toyota Crown с гибридной установкой.'},
            {'brand': 'Toyota', 'model': 'Crown', 'year': 2024, 'price': 7500000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'rear', 'fuel': 'hybrid', 'engine_volume': 2.5, 'power': 249, 'color': 'Белый', 'is_new': True, 'description': 'Премиальный седан с кожаным салоном и панорамной крышей.'},
            
            # Toyota bZ3X (2 авто)
            {'brand': 'Toyota', 'model': 'bZ3X', 'year': 2024, 'price': 5000000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'electric', 'engine_volume': 0.0, 'power': 204, 'color': 'Белый', 'is_new': True, 'description': 'Электрический кроссовер Toyota bZ3X — будущее уже здесь.'},
            {'brand': 'Toyota', 'model': 'bZ3X', 'year': 2024, 'price': 5200000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'electric', 'engine_volume': 0.0, 'power': 204, 'color': 'Синий', 'is_new': True, 'description': 'Электромобиль с запасом хода до 500 км.'},
            
            # Toyota Hilux (3 авто)
            {'brand': 'Toyota', 'model': 'Hilux', 'year': 2024, 'price': 6000000, 'mileage': 0, 'transmission': 'manual', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 2.8, 'power': 204, 'color': 'Серый', 'is_new': True, 'description': 'Легендарный пикап Toyota Hilux — надежность и выносливость.'},
            {'brand': 'Toyota', 'model': 'Hilux', 'year': 2024, 'price': 6200000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 2.8, 'power': 204, 'color': 'Белый', 'is_new': True, 'description': 'Пикап с автоматической коробкой передач.'},
            {'brand': 'Toyota', 'model': 'Hilux', 'year': 2023, 'price': 5500000, 'mileage': 10000, 'transmission': 'manual', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 2.8, 'power': 204, 'color': 'Черный', 'is_new': False, 'description': 'Надежный пикап, обслуживался у официального дилера.'},
            
            # Toyota RAV4 (3 авто)
            {'brand': 'Toyota', 'model': 'RAV4', 'year': 2024, 'price': 4200000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'hybrid', 'engine_volume': 2.5, 'power': 218, 'color': 'Синий', 'is_new': True, 'description': 'Популярный кроссовер Toyota RAV4 с гибридным двигателем.'},
            {'brand': 'Toyota', 'model': 'RAV4', 'year': 2024, 'price': 4400000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'hybrid', 'engine_volume': 2.5, 'power': 218, 'color': 'Белый', 'is_new': True, 'description': 'Кроссовер с полным приводом и гибридной установкой.'},
            {'brand': 'Toyota', 'model': 'RAV4', 'year': 2023, 'price': 3800000, 'mileage': 8000, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'gasoline', 'engine_volume': 2.0, 'power': 174, 'color': 'Красный', 'is_new': False, 'description': 'Кроссовер в хорошем состоянии, полный привод.'},
            
            # Toyota Raize (2 авто)
            {'brand': 'Toyota', 'model': 'Raize', 'year': 2024, 'price': 2500000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'gasoline', 'engine_volume': 1.0, 'power': 116, 'color': 'Оранжевый', 'is_new': True, 'description': 'Компактный кроссовер Toyota Raize для города.'},
            {'brand': 'Toyota', 'model': 'Raize', 'year': 2024, 'price': 2600000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'gasoline', 'engine_volume': 1.0, 'power': 116, 'color': 'Серый', 'is_new': True, 'description': 'Компактный кроссовер с полным приводом.'},
            
            # Toyota Camry (3 авто)
            {'brand': 'Toyota', 'model': 'Camry', 'year': 2024, 'price': 5000000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'gasoline', 'engine_volume': 2.5, 'power': 200, 'color': 'Черный', 'is_new': True, 'description': 'Бизнес-седан Toyota Camry — комфорт и статус.'},
            {'brand': 'Toyota', 'model': 'Camry', 'year': 2024, 'price': 5200000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'gasoline', 'engine_volume': 3.5, 'power': 249, 'color': 'Белый', 'is_new': True, 'description': 'Седан с двигателем V6 и кожаным салоном.'},
            {'brand': 'Toyota', 'model': 'Camry', 'year': 2023, 'price': 4500000, 'mileage': 6000, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'gasoline', 'engine_volume': 2.5, 'power': 200, 'color': 'Синий', 'is_new': False, 'description': 'Седан в отличном состоянии, полный пакет опций.'},
            
            # Toyota Corolla (3 авто)
            {'brand': 'Toyota', 'model': 'Corolla', 'year': 2024, 'price': 3200000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'gasoline', 'engine_volume': 1.6, 'power': 122, 'color': 'Серебристый', 'is_new': True, 'description': 'Надежный седан Toyota Corolla — выбор миллионов.'},
            {'brand': 'Toyota', 'model': 'Corolla', 'year': 2024, 'price': 3400000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'hybrid', 'engine_volume': 1.8, 'power': 140, 'color': 'Белый', 'is_new': True, 'description': 'Гибридный седан с низким расходом топлива.'},
            {'brand': 'Toyota', 'model': 'Corolla', 'year': 2023, 'price': 2800000, 'mileage': 7000, 'transmission': 'automatic', 'drive': 'front', 'fuel': 'gasoline', 'engine_volume': 1.6, 'power': 122, 'color': 'Красный', 'is_new': False, 'description': 'Седан в отличном техническом состоянии.'},
            
            # Toyota Fortuner (3 авто)
            {'brand': 'Toyota', 'model': 'Fortuner', 'year': 2024, 'price': 7500000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 2.8, 'power': 204, 'color': 'Белый', 'is_new': True, 'description': 'Рамный внедорожник Toyota Fortuner для бездорожья.'},
            {'brand': 'Toyota', 'model': 'Fortuner', 'year': 2024, 'price': 7800000, 'mileage': 0, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 2.8, 'power': 204, 'color': 'Черный', 'is_new': True, 'description': 'Внедорожник с кожаным салоном и люком.'},
            {'brand': 'Toyota', 'model': 'Fortuner', 'year': 2023, 'price': 6800000, 'mileage': 5000, 'transmission': 'automatic', 'drive': 'full', 'fuel': 'diesel', 'engine_volume': 2.8, 'power': 204, 'color': 'Серый', 'is_new': False, 'description': 'Внедорожник с минимальным пробегом, как новый.'},
        ]

        for car_data in cars_data:
            Car.objects.get_or_create(**car_data)
        
        self.stdout.write(self.style.SUCCESS(f'Добавлено {len(cars_data)} автомобилей в базу данных'))