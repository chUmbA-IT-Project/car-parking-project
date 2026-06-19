import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import Car

media_path = 'media/cars/'
files = os.listdir(media_path)
updated = 0

name_map = {
    'landcruiser300': 'Land Cruiser 300',
    'gr86': 'GR86',
    'crown': 'Crown',
    'bz3x': 'bZ3X',
    'hilux': 'Hilux',
    'rav4': 'RAV4',
    'raize': 'Raize',
    'camry': 'Camry',
    'corolla': 'Corolla',
    'fortuner': 'Fortuner',
}

for f in files:
    if not f.endswith(('.jpg', '.jpeg', '.png')):
        continue
    
    name_no_ext = f.replace('.jpg','').replace('.jpeg','').replace('.png','')
    # toyota_landcruiser300 -> ['toyota', 'landcruiser300']
    parts = name_no_ext.split('_', 1)
    if len(parts) != 2:
        print(f'SKIP: {f} - wrong format')
        continue
    
    brand_search = parts[0].capitalize()
    model_key = parts[1].lower()
    model_search = name_map.get(model_key, model_key.capitalize())
    
    cars = Car.objects.filter(brand__iexact=brand_search, model__iexact=model_search)
    count = cars.count()
    for car in cars:
        car.main_image = 'cars/' + f
        car.save()
        updated += 1
    print(f'OK: {brand_search} {model_search} ({count} шт) -> {f}')

print(f'\nВсего обновлено: {updated} автомобилей')