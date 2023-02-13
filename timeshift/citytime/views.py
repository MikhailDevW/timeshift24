from django.shortcuts import render

from citytime import timeshift_lib as ts
from .models import City, Update

import datetime
from datetime import datetime


def index(request):
    template = 'index.html'
    month: dict = {
        '1': 'января',
        '2': 'февраля',
        '3': 'марта',
        '4': 'апреля',
        '5': 'мая',
        '6': 'июня',
        '7': 'июля',
        '8': 'августа',
        '9': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря',
    }

    # Если поступил POST запрос
    if request.method == 'POST':
        city_name = request.POST['city_name'].lower().capitalize()
        api = ts.AbstractAPI()
        response_data = api.fetch_city_data(city_name)

        # Если нет ошибки и город через API найден
        # а также строка содержит только алфавитные символы
        if not response_data.get('error', False):
            city_time = datetime.strptime(
                response_data['datetime'],
                '%Y-%m-%d %H:%M:%S')
            data = {
                'name': city_name,
                'hours': str(city_time.hour).zfill(2),
                'minutes': str(city_time.minute).zfill(2),
                'seconds': str(city_time.second).zfill(2),
                'date': city_time.day,
                'month': month[str(city_time.month)],
                'year': city_time.year,
            }
            return render(request, template, data)
        # в случае если город не найден через апи
        else:
            data = {
                'name': 'Не найден',
                'hours': '--',
                'minutes': '--',
                'seconds': '--',
            }
            return render(request, template, data)
    else:
        api = ts.AbstractAPI()
        response_data = api.fetch_city_data('Moscow')
        city_time = datetime.strptime(
                response_data['datetime'],
                '%Y-%m-%d %H:%M:%S')
        data = {
            'name': 'Москва',
            'hours': str(city_time.hour).zfill(2),
            'minutes': str(city_time.minute).zfill(2),
            'seconds': str(city_time.second).zfill(2),
            'date': city_time.day,
            'month': month[str(city_time.month)],
            'year': city_time.year,
        }
        return render(request, template, data)


def allcities(request):
    template = 'allcities.html'
    cities = City.objects.all()[:10]
    # api = ts.AbstractAPI()
    # utc_time = datetime.now(datetime.timezone.utc)
    # В словаре context отправляем информацию в шаблон
    context = {
        'cities': cities,
    }
    return render(request, template, context)

    # utc_time = datetime.now(datetime.timezone.utc)
    # В словаре context отправляем информацию в шаблон
    # context = {
    #    'cities': cities,
    #    'utc': utc_time,
    #    'hours': int(utc_time.strftime('%H')),
    #    'minutes': utc_time.strftime('%M'),


def news(request):
    template = 'news.html'
    news = Update.objects.all()[:10]

    context = {
        'news': news,
    }
    return render(request, template, context)
