from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(
        max_length=50,
        db_index=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'company_slug': self.slug})


class Sneakers(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='sneakers',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=150,
        db_index=True,
    )
    slug = models.CharField(
        max_length=100,
        unique=True,
        db_index=True
    )
    img = models.ImageField(
        upload_to='sneakers_img/',
        blank=True,
    )
    description = models.TextField(
        max_length=1000,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
    available = models.BooleanField(
        default=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ('name', 'price',)
        verbose_name = 'Кроссовки'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:sneakers_detail', args=[self.id, self.slug])


class Comments(models.Model):
    comment_text = models.CharField(
        max_length=1000,
        verbose_name='Ваш комментарий'
    )
    comment_time = models.DateTimeField(
        auto_now_add=True
    )
    comment_model = models.ForeignKey(
        Sneakers,
        on_delete=models.CASCADE,
        related_name='some_comment'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

        def __str__(self):
            return self.comment_text

