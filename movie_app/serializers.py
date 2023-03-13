from django.contrib.auth.models import User

from .models import Director, Movie, Review
from rest_framework import serializers
from rest_framework.exceptions import ValidationError



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars movie_title movie_id'.split()


class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title description duration director  movie_reviews average_score'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.CharField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('This Director does not exist')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(max_value=5, min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('This Movie does not exist')
        return movie_id

