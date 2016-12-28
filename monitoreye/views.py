#coding:utf-8

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from service_manage.models import Service

def monitor_index(request):
    service_machine_list = Service.objects.all()
    service_count = Service.objects.count()
    return render_to_response('default/default_new.html', locals())
