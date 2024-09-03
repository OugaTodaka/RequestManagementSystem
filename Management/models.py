from django.db import models
# Create your models here.

class Request(models.Model):
    STATUS_CHOICES = [
        (0, '要望受付'),
        (1, '制作途中'),
        (2, '制作完了'),
    ]

    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    system_name = models.CharField(max_length=100, null=False, blank=False, default='default')
    system_overview = models.CharField(max_length=1000, null=False, blank=False, default='default')
    mail = models.EmailField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now_add=True, null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.system_name
