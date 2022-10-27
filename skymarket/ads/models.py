from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ad(models.Model):
    title = models.CharField(max_length=50)
    price = models.SmallIntegerField()
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
