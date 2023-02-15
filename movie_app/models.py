from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    duration = models.CharField(max_length=255, verbose_name='Длительность')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='Режиссер')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return str(self.movie)
