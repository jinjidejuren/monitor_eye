from django.contrib import admin

# Register your models here.

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    fields = ['service_machine_name', 'inside_ip', 'outside_up','service_group',
              'cpu_num', 'memory_size', 'disk_size', 'bandwidth', 'create_time' ]
    list_display = ('service_machine_name', 'outside_up', 'inside_ip', 'create_time')
    search_fields = ['service_machine_name']
    list_filter = ['create_time']   
 

admin.site.register(Service, ServiceAdmin)


