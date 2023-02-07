from django.shortcuts import render
from django.http import HttpResponse

from citytime import timeshift_lib as ts
# Create your views here.
# Главная страница


def index(request):
    template = 'index.html'
    response_data = dict()

    if request.method == 'POST':
        city_name = request.POST['city_name']
        api = ts.AbstractAPI()
        response_data = api.fetch_city_data(city_name)
        
        if not response_data.get('error', False):
            response_data['local_time'] = api.get_local_time(
                response_data['gmt_offset']
            )
        print(response_data)
        return render(request, template, response_data)
    else:
        response_data['name'] = 'Москва'
        api = ts.AbstractAPI()
        response_data['local_time'] = api.get_local_time(3)
        return render(request, template, response_data)

    #response_data['city'] = 'Moscow'
    #api = ts.AbstractAPI()
    #response_data['local_time'] = api.get_local_time(3)

    #print('>>>', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    #return render(request, template, response_data)

def fetch_city():
    ...