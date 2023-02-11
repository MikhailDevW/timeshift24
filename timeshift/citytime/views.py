from django.shortcuts import render

from citytime import timeshift_lib as ts
from .models import City

import datetime


def index(request):
    template = 'index.html'
    response_data = dict()
    data = dict()
    month: dict = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
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
        if not response_data.get('error', False):
            data = {
                'name': city_name,
                'hours': response_data['datetime'][11: 13],
                'minutes': response_data['datetime'][14: 16],
                'seconds': response_data['datetime'][17:],
                'date': response_data['datetime'][8:10],
                'month': month[response_data['datetime'][5:7]],
                'year': response_data['datetime'][:4],
            }
            return render(request, template, data)
        # в случае если город не найден через апи
        else:
            data = {
                'name': 'Не найден',
                'local_time': '--:--',
            }
            return render(request, template, data)
    else:
        api = ts.AbstractAPI()
        response_data = api.fetch_city_data('Moscow')
        data = {
            'name': 'Москва',
            'hours': response_data['datetime'][11: 13],
            'minutes': response_data['datetime'][14: 16],
            'seconds': response_data['datetime'][17:],
            'date': response_data['datetime'][8:10],
            'month': month[response_data['datetime'][5:7]],
            'year': response_data['datetime'][:4],
        }
        return render(request, template, data)


def allcities(request):
    template = 'allcities.html'
    cities = City.objects.all()[:10]
    # api = ts.AbstractAPI()
    utc_time = datetime.datetime.now(datetime.timezone.utc)
    # В словаре context отправляем информацию в шаблон
    context = {
        'cities': cities,
        'utc': utc_time,
        'hours': int(utc_time.strftime('%H')),
        'minutes': utc_time.strftime('%M'),
    }
    return render(request, template, context)
