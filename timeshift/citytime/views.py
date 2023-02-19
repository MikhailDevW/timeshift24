from django.shortcuts import render

from citytime import timeshift_lib as ts
from .models import City, Update

from datetime import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, 'ru')


def index(request):
    api = ts.AbstractAPI()
    template = 'index.html'

    # Если поступил POST запрос
    if request.method == 'POST':
        city_name = request.POST['city_name'].capitalize()
        response_data = api.fetch_city_data(city_name)

        # Если нет ошибки и город через API найден
        # а также строка содержит только алфавитные символы
        if not response_data.get('error', False):
            city_dt = dt.strptime(
                response_data['datetime'],
                '%Y-%m-%d %H:%M:%S'
            )
            offset = response_data['gmt_offset']
            date = city_dt.strftime('%d %B %Y')
            data = {
                'date': date,
                'name': city_name,
                'offset': offset,
            }
            return render(request, template, data)
        # в случае если город не найден через апи
        else:
            return render(request, template, {'name': city_name})
    else:
        response_data = api.fetch_city_data('Moscow')
        if not response_data.get('error', False):
            city_dt = dt.strptime(
                response_data['datetime'],
                '%Y-%m-%d %H:%M:%S'
            )
            offset = response_data['gmt_offset']
            date = city_dt.strftime('%d %B %Y')
            data = {
                'date': date,
                'name': 'Москва',
                'offset': offset
            }
            return render(request, template, data)
        else:
            return render(request, template, {'name': 'APIError'})


def allcities(request):
    template = 'allcities.html'
    cities = City.objects.all()[:10]
    # api = ts.AbstractAPI()
    # utc_time = dt.now(tz.utc)

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


def contact(request):
    template = 'news.html'

    return render(request, template)


def about(request):
    template = 'news.html'

    return render(request, template)
