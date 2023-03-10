import django.db.utils
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, \
    MovieValidateSerializer, DirectorValidateSerializer, ReviewValidateSerializer
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
        data = request.data
        if data:
            if len(data) > 1:
                validation = [DirectorValidateSerializer(data=elem).is_valid
                              (raise_exception=True) for elem in data]
                for name in data:
                    Director.objects.create(
                        name=name['name']
                    )
                return Response(data='objects created')
            serializer = DirectorValidateSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            Director.objects.create(
                name=serializer.validated_data.get('name')
            )
            return Response(data='object created')
        if not data:
            serializer = DirectorValidateSerializer(data=data)
            serializer.is_valid(raise_exception=True)


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
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        director.name = serializer.validated_data.get('name')
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
        data = request.data
        if data:
            if type(data) == list:
                validation = [MovieValidateSerializer(data=elem).is_valid
                              (raise_exception=True) for elem in data]
                for item in data:
                    Movie.objects.create(
                        title=item.get('title'),
                        description=item.get('description'),
                        duration=item.get('duration'),
                        director_id=item.get('director_id')
                    )
                return Response(data='objects created')
            else:
                serializer = MovieValidateSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                Movie.objects.create(
                    title=serializer.validated_data.get('title'),
                    description=serializer.validated_data.get('description'),
                    duration=serializer.validated_data.get('duration'),
                    director_id=serializer.validated_data.get('director_id')
                )
                return Response(data='object created')
        else:
            serializer = MovieValidateSerializer(data=data)
            serializer.is_valid(raise_exception=True)


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
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = serializer.validated_data.get('title')
        movie.duration = serializer.validated_data.get('duration')
        movie.description = serializer.validated_data.get('description')
        movie.director_id = serializer.validated_data.get('director_id')
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
        data = request.data
        if data:
            if type(data) == list:
                validation = [ReviewValidateSerializer(data=elem).is_valid
                              (raise_exception=True) for elem in data]
                for item in data:
                    Review.objects.create(
                        text=item.get('text'),
                        movie_id=item.get('movie_id'),
                        stars=item.get('stars')
                    )
                return Response(data='objects created')
            else:
                serializer = ReviewValidateSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                Review.objects.create(
                    text=serializer.validated_data.get('text'),
                    movie_id=serializer.validated_data.get('movie_id'),
                    stars=serializer.validated_data.get('stars')
                )
                return Response(data='object created')
        else:
            serializer = ReviewValidateSerializer(data=data)
            serializer.is_valid(raise_exception=True)


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
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.stars = serializer.validated_data.get('stars')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.text = serializer.validated_data.get('text')
        review.save()
        return Response(data={'message': 'Review received'},
                        status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        return Response(data={'message': 'object deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def show_movies_reviews(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)
