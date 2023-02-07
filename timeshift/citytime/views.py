from django.shortcuts import render
from django.http import HttpResponse

import os

# Create your views here.
# Главная страница
def index(request):    
    template = 'index.html'
    
    
    print('>>>', os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    context = {
        # В словарь можно передать переменную
        'city': 'gdfdgfg',
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'date': '6',
    }
    return render(request, template, context)