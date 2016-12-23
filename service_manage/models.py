#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Service(models.Model):
    service_machine_name = models.CharField(u'服务器名称', max_length=50)
    inside_ip = models.CharField(u'内网ip', max_length=40)
    outside_up = models.CharField(u'外网ip',max_length=40)
    service_group = models.CharField(u'服务器组', max_length=40)
    cpu_num = models.IntegerField()
    memory_size = models.IntegerField()
    disk_size = models.IntegerField()
    bandwidth = models.IntegerField()
    create_time = models.DateTimeField(u'创建时间')

    def __unicode__(self):
        return self.service_machine_name 
