from django.db import models

class News(models.Model):
    judul = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(auto_now=True, null=False, blank=False)
    topik = models.ManyToManyField('Topik', blank=False)
    konten = models.TextField(null=False, blank=False)
    TYPE_STATUS = (
        ('PUBLISH','Publish'),
        ('DRAFT','Draft'),
        ('DELETE','Delete')
    )
    status = models.CharField(max_length=20, choices=TYPE_STATUS, default="DRAFT")

    def __str__(self):
        return self.judul

class Topik(models.Model):
    judulTopik = models.CharField(max_length=100, null= False, blank=False)

    def __str__(self):
        return self.judulTopik