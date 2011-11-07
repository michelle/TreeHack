from django.db import models

class Code(models.Model):
    rawcode = models.CharField(max_length = 99999, blank=True)
    serialcode = models.CharField(max_length = 99999, blank=True)
