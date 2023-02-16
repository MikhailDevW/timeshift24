from django.shortcuts import render

from citytime import timeshift_lib as ts
from .models import City


from datetime import datetime as dt, timezone as tz
import locale

locale.setlocale(locale.LC_TIME, 'ru')


def index(request):
    api = ts.AbstractAPI()
    template = 'index.html'

    # Если поступил POST запрос
    if request.method == 'POST':
        city_name = request.POST['city_name'].capitalize()
        response_data = api.fetch_city_data(city_name)

        # Если нет ошибки и город через API найден
        if not response_data.get('error', False):
            city_dt = dt.strptime(
                response_data['datetime'],
                '%Y-%m-%d %H:%M:%S'
            )
            date = city_dt.strftime('%d %B %Y')
            data = {
                'date': date,
                'name': city_name,
                'time': city_dt,
            }
            return render(request, template, data)
        # в случае если город не найден через апи
        else:
            data = {
                'local_time': '--:--',
                'name': 'Не найден',
            }
            return render(request, template, data)
    else:
        response_data = api.fetch_city_data('Moscow')
        city_dt = dt.strptime(response_data['datetime'], '%Y-%m-%d %H:%M:%S')
        date = city_dt.strftime('%d %B %Y')
        data = {
            'date': date,
            'name': 'Москва',
            'time': city_dt,
        }
        return render(request, template, data)


def allcities(request):
    template = 'allcities.html'
    cities = City.objects.all()[:10]
    # api = ts.AbstractAPI()
    utc_time = dt.now(tz.utc)
    # В словаре context отправляем информацию в шаблон
    context = {
        'cities': cities,
        'utc': utc_time,
        'hours': int(utc_time.strftime('%H')),
        'minutes': utc_time.strftime('%M'),
    }
    return render(request, template, context)
