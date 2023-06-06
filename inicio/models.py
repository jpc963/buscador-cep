from django.db import models


class Cep(models.Model):
    cep = models.CharField(max_length=8)
    state = models.CharField(max_length=2, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    neighborhood = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    searched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cep
