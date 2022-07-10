from rest_framework import serializers
from app_movie.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews rating'.split()


class DirectorCountSerialize(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movie_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()


