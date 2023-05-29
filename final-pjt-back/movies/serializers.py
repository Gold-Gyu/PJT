from rest_framework import serializers
from .models import Movie, Review, Genre
from django.contrib.auth import get_user_model


# 리뷰 내용
class Movie_reviewaddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("title", "content",)


# 장르
class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")

class MovieListSerializer(serializers.ModelSerializer):
    
    genre_ids = GenreListSerializer(many=True)
    class Meta:
        model = Movie
        fields =  fields = ('id','title', 'overview', 'release_date', 'poster_path', 'popularity', 'vote_average', 'genre_ids')

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

# 유저 이름과 id
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('id', 'username')


class title_from_movie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)

class ReviewListSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Review
        fields = ("id", "rank", "content", "created_at", "movie", "userId", "username")

class ReviewSerializer(serializers.ModelSerializer):
    movie = title_from_movie_Serializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"

class Movie_reviewcreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        
class Movie_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class Movie_reviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id','content', 'rank', 'user',)
        read_only_fields = ('user',)

class MovieDetailSerializer(serializers.ModelSerializer):
    comment_set = Movie_reviewSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id','title','overview','release_date','vote_average','poster_path','like','comment_set')