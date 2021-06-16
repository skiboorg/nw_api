from django.db import models


class Banner(models.Model):
    order = models.IntegerField(default=10)
    top_text = models.CharField(max_length=255, blank=True, null=True)
    bottom_text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение', upload_to='images/banner/', blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)


class Faq(models.Model):
    order = models.IntegerField(default=100)
    question = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

