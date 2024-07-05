from django.db import models
<<<<<<< HEAD
 
=======

>>>>>>> 8192be7290ac9de8e4dfe2ee5837d9af591d43e7

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    mail = models.EmailField(max_length=100, null=False, blank=False)
    system_name = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
<<<<<<< HEAD
 
 
=======


>>>>>>> 8192be7290ac9de8e4dfe2ee5837d9af591d43e7
class RequestFunction(models.Model):
    function_id = models.AutoField(primary_key=True)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    function_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=400, null=False, blank=False)
