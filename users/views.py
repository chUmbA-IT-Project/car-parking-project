from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Car, ContactRequest, Notification, UserProfile


def home(request):
    # Карусель использует базовые фото (без суффиксов _1/_2/_3)
    carousel_models = ['Land Cruiser 300', 'GR86', 'Crown', 'bZ3X', 'Hilux']
    base_images = {
        'Land Cruiser 300': 'cars/toyota_landcruiser300.jpg',
        'GR86': 'cars/toyota_gr86.jpg',
        'Crown': 'cars/toyota_crown.jpg',
        'bZ3X': 'cars/toyota_bz3x.jpg',
        'Hilux': 'cars/toyota_hilux.jpg',
    }
    carousel_cars = []
    for model_name in carousel_models:
        car = Car.objects.filter(model=model_name, is_available=True).first()
        if car:
            # Для карусели подставляем базовое фото
            car.carousel_image = base_images.get(model_name)
            carousel_cars.append(car)
    
    context = {
        'carousel_cars': carousel_cars,
    }
    return render(request, 'home.html', context)


def models_list(request):
    cars = Car.objects.filter(is_available=True)
    brands = Car.objects.values_list('brand', flat=True).distinct().order_by('brand')
    context = {
        'cars': cars,
        'brands': brands,
    }
    return render(request, 'models_list.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {'car': car}
    return render(request, 'car_detail.html', context)


def available_cars(request):
    cars = Car.objects.filter(is_available=True)
    brands = Car.objects.values_list('brand', flat=True).distinct().order_by('brand')
    
    brand_filter = request.GET.get('brand')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    fuel_type = request.GET.get('fuel')
    transmission = request.GET.get('transmission')
    
    if brand_filter:
        cars = cars.filter(brand=brand_filter)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if fuel_type:
        cars = cars.filter(fuel=fuel_type)
    if transmission:
        cars = cars.filter(transmission=transmission)
    
    context = {
        'cars': cars,
        'brands': brands,
        'current_filters': request.GET,
    }
    return render(request, 'available_cars.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        ContactRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message,
        )
        messages.success(request, 'Ваша заявка на консультацию успешно отправлена! Мы свяжемся с вами в ближайшее время.')
        return redirect('contacts')
    
    return render(request, 'contacts.html')


def about(request):
    return render(request, 'about.html')


def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('login_input')
        password = request.POST.get('password')
        
        user = None
        if '@' in login_input:
            try:
                user_obj = User.objects.get(email=login_input)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        else:
            user = authenticate(username=login_input, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.first_name or user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Неверный email/телефон или пароль.')
    
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        last_name = request.POST.get('last_name', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip().lower()
        password1 = request.POST.get('password1', '').strip()
        password2 = request.POST.get('password2', '').strip()
        
        # Валидация
        if not email or not password1 or not password2:
            messages.error(request, 'Заполните все обязательные поля.')
            return render(request, 'register.html')
        
        if password1 != password2:
            messages.error(request, 'Пароли не совпадают.')
            return render(request, 'register.html')
        
        if len(password1) < 8:
            messages.error(request, 'Пароль должен быть минимум 8 символов.')
            return render(request, 'register.html')
        
        if User.objects.filter(username=email).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже зарегистрирован.')
            return render(request, 'register.html')
        
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
            )
        except Exception as e:
            messages.error(request, f'Ошибка создания пользователя: {str(e)}')
            return render(request, 'register.html')
        
        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.phone = phone
        profile.save()

        # Бонус за регистрацию
        Notification.objects.create(
            user=user,
            title='Бонус за регистрацию',
            message='Спасибо за регистрацию! Вы получили бесплатную экспресс-консультацию по модели Toyota.',
            notification_type='bonus',
        )
        
        login(request, user)
        messages.success(request, f'Регистрация успешна! Добро пожаловать, {first_name}!')
        return redirect('home')
    
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('home')


def password_reset(request):
    return render(request, 'password_reset.html')


@login_required
def profile(request):
    context = {}
    return render(request, 'profile.html', context)


@login_required
def notifications(request):
    all_notifications = request.user.notifications.all()
    unread_count = all_notifications.filter(is_read=False).count()
    
    if request.method == 'POST':
        notif_id = request.POST.get('notification_id')
        action = request.POST.get('action')
        
        if action == 'mark_read' and notif_id:
            notif = get_object_or_404(Notification, id=notif_id, user=request.user)
            notif.is_read = True
            notif.save()
    
    context = {
        'notifications': all_notifications,
        'unread_count': unread_count,
    }
    return render(request, 'notifications.html', context)


@login_required
def profile_settings(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        
        profile = user.profile
        profile.phone = request.POST.get('phone', '')
        if request.FILES.get('avatar'):
            profile.avatar = request.FILES['avatar']
        profile.save()
        
        messages.success(request, 'Настройки успешно сохранены!')
        return redirect('profile_settings')
    
    return render(request, 'profile_settings.html')