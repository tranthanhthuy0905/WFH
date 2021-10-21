from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class reportTracking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #domain = models.ForeignKey(User, on_delete=models.CASCADE)
    domain=models.CharField(max_length=30, null=False, blank=False)
    tasks = models.TextField(null=False, blank=False)
    code_commit = models.TextField(null=True, blank=True)
    docs = models.TextField(null=True, blank=True)
    #slug = models.SlugField(null=True) #new

    #def get_absolute_url(self):
        #return reverse('report_detail', kwargs={'slug': self.domain})

    def __str__(self):
        return self.domain
    def __str__(self):
        return self.tasks

