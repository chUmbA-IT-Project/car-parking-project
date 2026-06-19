from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'Профиль {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('manual', 'Механика'),
        ('automatic', 'Автомат'),
        ('robot', 'Робот'),
        ('variator', 'Вариатор'),
    ]
    FUEL_CHOICES = [
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'),
        ('electric', 'Электро'),
    ]
    DRIVE_CHOICES = [
        ('fwd', 'Передний привод'),
        ('rwd', 'Задний привод'),
        ('awd', 'Полный привод'),
    ]

    brand = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=100)
    year = models.IntegerField('Год выпуска')
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    mileage = models.IntegerField('Пробег, км', default=0)
    engine_volume = models.DecimalField('Объем двигателя, л', max_digits=3, decimal_places=1)
    power = models.IntegerField('Мощность, л.с.')
    transmission = models.CharField('КПП', max_length=20, choices=TRANSMISSION_CHOICES)
    drive = models.CharField('Привод', max_length=20, choices=DRIVE_CHOICES)
    fuel = models.CharField('Топливо', max_length=20, choices=FUEL_CHOICES)
    color = models.CharField('Цвет', max_length=50)
    description = models.TextField('Описание', blank=True)
    is_available = models.BooleanField('В наличии', default=True)
    is_new = models.BooleanField('Новинка', default=False)
    main_image = models.ImageField('Главное фото', upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Фото', upload_to='cars/')
    order = models.IntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Фото автомобиля'
        verbose_name_plural = 'Фото автомобилей'
        ordering = ['order']

    def __str__(self):
        return f'Фото {self.car}'


class ContactRequest(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', blank=True)
    message = models.TextField('Сообщение', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_read = models.BooleanField('Прочитано', default=False)

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'
        ordering = ['-created_at']

    def __str__(self):
        return f'Заявка от {self.name}'


class Notification(models.Model):
    TYPE_CHOICES = [
        ('promo', 'Акция'),
        ('bonus', 'Бонус'),
        ('info', 'Информация'),
        ('alert', 'Предупреждение'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name='Пользователь')
    title = models.CharField('Заголовок', max_length=200)
    message = models.TextField('Сообщение')
    notification_type = models.CharField('Тип', max_length=20, choices=TYPE_CHOICES, default='info')
    is_read = models.BooleanField('Прочитано', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} → {self.user.username}'


class ConsultationRequest(models.Model):
    """Заявка на консультацию по конкретному автомобилю"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', blank=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автомобиль')
    message = models.TextField('Сообщение', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_read = models.BooleanField('Прочитано', default=False)

    class Meta:
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'
        ordering = ['-created_at']

    def __str__(self):
        return f'Консультация от {self.name} {"по " + str(self.car) if self.car else ""}'