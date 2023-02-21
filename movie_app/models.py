from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')

    def __str__(self):
        return self.name

    def movies_count(self):
        res = Movie.objects.filter(director=self.id)
        return len(res)


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    duration = models.CharField(max_length=255, verbose_name='Длительность')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='Режиссер')

    def __str__(self):
        return self.title

    def get_reviews(self):
        return Review.objects.filter(movie = self.id)

    def average_score(self):
        get_stars = self.get_reviews()
        if get_stars:
            review_score = [review.stars for review in get_stars]
            average = sum(review_score)/len(review_score)
            return round(average)
        else:
            return ''


class Review(models.Model):
    text = models.TextField(verbose_name='Отзыв')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='фильм', related_name='movie_reviews')
    stars = models.IntegerField(choices=(
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    ), verbose_name='Рейтинг', default=5)

    def __str__(self):
        return str(self.movie)



