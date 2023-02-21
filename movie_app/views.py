from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from .models import Director, Movie, Review


@api_view(['GET'])
def test(request):
    return Response('OK')


@api_view(['GET'])
def directors_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def detail_director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': f'Director object with id = {id} not found'})
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def detail_movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': f'Movie object with id = {id} not found'})
    data = MovieSerializer(movie).data
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def detail_review(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': f'Review object with id = {id} not found'})
    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view(['GET'])
def show_movies_reviews(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data=data)