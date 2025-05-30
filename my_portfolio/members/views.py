# from django.shortcuts import render
# from tempfile import template
from django.http import HttpResponse
from django.template import loader

#메인
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

#numpy
import numpy as np
from django.shortcuts import render

def ifelse(request):
    template = loader.get_template('ifelse.html')
    context = {
        'greeting':2,
    }
    return HttpResponse(template.render(context, request))

def syntax(request):
    template = loader.get_template('syntax.html')
    context = {
        'firstname':'진히',
        'lastname':'이',
    }
    return HttpResponse(template.render(context, request))

def members(request):
    template = loader.get_template('members.html')
    return HttpResponse(template.render())

    arr = np.array([1, 2, 3, 4, 5])  # 배열생성
    total = np.sum(arr)  # 배열의총합
    mean = np.mean(arr)  # 배열의평균

    context = {
        'greeting':'hello, Members!',
        'total':total,
        'mean':mean
    }

    # 결과를 템플릿으로 전달
    return render(request, 'members.html',context)

def forloop(request):
    template = loader.get_template('forloop.html')
    context = {
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }]
    }
    return HttpResponse(template.render(context, request))