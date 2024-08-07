from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from extensions.utils import jalali_converter


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=300, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ("position",)
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:category_list", kwargs={"category_slug": self.slug})


class Post(models.Model):
    STATUS_CHOICES = (("draft", "پیشنویس"), ("published", "منتشر شده"))
    title = models.CharField(max_length=250, verbose_name="عنوان")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    thumbnail = models.ImageField(
        upload_to="image", null=True, blank=True, verbose_name="تصویر"
    )
    slug = models.SlugField(max_length=300, unique=True)
    body = models.TextField(verbose_name="متن", null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        verbose_name="نویسنده",
    )
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=timezone.now, verbose_name="زمان ایجاد")
    updated = models.DateTimeField(auto_now=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
        verbose_name="وضعیت انتشار",
    )

    class Meta:
        ordering = ("-publish",)
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def get_category(self):
        return ", ".join([cat.title for cat in self.category.all()])

    get_category.short_description = "دسته بندی"

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            kwargs={
                "year": self.publish.year,
                "month": self.publish.month,
                "day": self.publish.day,
                "slug": self.slug,
            },
        )

    def jpublish(self):
        return jalali_converter(self.publish)

    def save(self, *args, **kwargs):
        thumbnail = self.thumbnail

        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
