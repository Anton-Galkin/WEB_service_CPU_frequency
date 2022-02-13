from django.db import models

# Create your models here.


class FrequencyCPU(models.Model):
    frequency = models.FloatField()
    # time_meter = models.DateTimeField(auto_now_add=True)


