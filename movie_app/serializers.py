from .models import Director, Movie, Review
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title description duration director  movie_reviews average_score'.split()



