from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','پیشنویس'),
        ('published','منتشر شده')
    )
    title = models.CharField(max_length=250,verbose_name='عنوان')
    thumbnail = models.ImageField(upload_to= 'image', null = True, blank=True, verbose_name='تصویر')
    slug = models.SlugField(max_length=300)
    body = models.TextField(verbose_name='متن',null = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='blog_posts',
                               verbose_name='نویسنده')
    publish = models.DateTimeField(default= timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add = timezone.now, verbose_name= 'زمان ایجاد')
    updated = models.DateTimeField(auto_now= timezone.now)
    status = models.CharField(max_length= 10, choices=STATUS_CHOICES, default='draft',
                              verbose_name='وضعیت انتشار')
    
    class Meta:
        ordering = ('-publish',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title