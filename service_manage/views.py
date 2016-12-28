#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from service_manage.models import Service


# def index(request):
#     service_machine_list = Service.objects
#     template = loader.get_template('service_manage/index.html')
#     context = RequestContext(request, {
#         'service_machine_list': service_machine_list,
#     })
#     return HttpResponse(template.render(context))


def service_index(request):
    service_machine_list = Service.objects.all()
    service_count = Service.objects.count()
    return render_to_response('service_manage/service_manage.html', locals())
