#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Service
from django.template import RequestContext, loader

def index(request):
    service_machine_list = Service.objects
    template = loader.get_template('service_manage/index.html')
    context = RequestContext(request, {
        'service_machine_list': service_machine_list,
    })
    return HttpResponse(template.render(context))
