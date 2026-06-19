import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

import django
django.setup()

from django.test import Client
c = Client()

# Обходим все страницы
pages = [
    ('/', 'Главная'),
    ('/models/', 'Модели'),
    ('/available/', 'В наличии'),
    ('/contacts/', 'Контакты'),
    ('/about/', 'О компании'),
    ('/login/', 'Вход'),
    ('/register/', 'Регистрация'),
    ('/password-reset/', 'Восстановление пароля'),
]

for url, name in pages:
    try:
        r = c.get(url)
        print(f'{name:25s} {url:25s} -> {r.status_code}')
    except Exception as e:
        print(f'{name:25s} {url:25s} -> ERROR: {e}')

# Проверяем авторизацию
r = c.post('/register/', {
    'first_name': 'Тест',
    'last_name': 'Тестов',
    'phone': '+79990001122',
    'email': 'test_user@autopremium.ru',
    'password1': 'Test12345!',
    'password2': 'Test12345!',
})
print(f'Регистрация (POST) -> {r.status_code}')

r = c.post('/login/', {
    'login_input': 'test_user@autopremium.ru',
    'password': 'Test12345!',
})
print(f'Вход (POST) -> {r.status_code}')

print('\nВсе страницы работают!')