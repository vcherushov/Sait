from django.db import models
from django.urls import reverse


class Avtobus(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    video = models.FileField(upload_to="video/%Y/%m/%d/")
    time_create = models.DateField(null=True, blank=True, verbose_name="Дата")
    time_time = models.TimeField(null=True, blank=True, verbose_name="Время")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Автобус")
    door = models.ForeignKey('Door', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Дверь")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Автобусы'
        verbose_name_plural = 'Автобусы'
        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Door(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('door', kwargs={'door_id': self.pk})
