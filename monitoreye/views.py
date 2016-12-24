#coding:utf-8

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext

def monitor_index(request):
    #return render_to_response('default/default_new.html', context_instance=RequestContext(request))
    return render_to_response('default/default_new.html')
