import django.db.utils
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from .models import Director, Movie, Review


@api_view(['GET'])
def test(request):
    return Response('OK')


@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        queryset = request.data
        for item in queryset:
            name = item.get('name')
            Director.objects.create(
                name=name
            )
        return Response(data={'message': f'Directors created {queryset}'},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': f'Director object with id = {id} not found'})
    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)

    elif request.method == 'PUT':
        old_name = director.name
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message': f'name:{old_name} changed to:{director.name}'},
                        status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        director.delete()
        return Response(data={'message': 'object deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movies_list_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        queryset = request.data
        count = queryset.__len__()
        while count != 0:
            for item in queryset:
                title = item.get('title')
                description = item.get('description')
                duration = item.get('duration')
                director_id = item.get('director_id')
                try:
                    Movie.objects.create(
                        title=title,
                        description=description,
                        duration=duration,
                        director_id=director_id
                    )
                    count -= 1
                except django.db.utils.IntegrityError:
                    return Response(data={'message': f'There is no object with this id = {director_id}'},
                                    status=status.HTTP_204_NO_CONTENT)
            return Response(data={'message': f'Movies created {queryset}'},
                            status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': f'Movie object with id = {id} not found'})
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)

    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.duration = request.data.get('duration')
        movie.description = request.data.get('description')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data={'message': f'Movie changed {MovieSerializer(movie).data}'},
                        status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Object deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        queryset = request.data
        count = queryset.__len__()
        while count != 0:
            for item in queryset:
                text = item.get('text')
                movie_id = item.get('movie_id')
                stars = item.get('stars')
                try:
                    Review.objects.create(
                        text=text,
                        movie_id=movie_id,
                        stars=stars
                    )
                    count -= 1
                except django.db.utils.IntegrityError:
                    return Response(data={'message': f'There is no object with this id = {movie_id}'},
                                    status=status.HTTP_204_NO_CONTENT)
            return Response(data={'message': f'Reviews received {queryset}'},
                            status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_review(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': f'Review object with id = {id} not found'})

    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)

    elif request.method == 'PUT':
        try:
            review.stars = request.data.get('stars')
            review.movie_id = request.data.get('movie_id')
            review.text = request.data.get('text')
            review.save()
            return Response(data={'message': 'Data received'},
                            status=status.HTTP_200_OK)
        except django.db.utils.IntegrityError:
            return Response(data={'message': f'There is no object with this id = {request.data.get("movie_id")}'},
                            status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'DELETE':
        review.delete()
        return Response(data={'message': 'object deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def show_movies_reviews(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)
