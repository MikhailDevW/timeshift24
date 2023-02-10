from django.shortcuts import render

from citytime import timeshift_lib as ts


def index(request):
    template = 'index.html'
    response_data = dict()
    data = dict()

    # Если поступил POST запрос
    if request.method == 'POST':
        city_name = request.POST['city_name']
        api = ts.AbstractAPI()
        response_data = api.fetch_city_data(city_name)

        # Если нет ошибки и город через API найден
        if not response_data.get('error', False):
            data = {
                'name': city_name,
                'local_time': response_data['datetime'][-8:],
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
            'local_time': response_data['datetime'][-8:],
        }
        print(response_data)
        return render(request, template, data)
