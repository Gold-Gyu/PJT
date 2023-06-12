from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import IsAuthenticaed
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from .models import Actor, Movie, Review, Genre
from .serializers import Movie_List_Serializer,ReviewListSerializer, MovieDetailSerializer, ReviewSerializer, Movie_reviewSerializer, MovieListSerializer, GenreListSerializer, MovieSerializer
from django.http import JsonResponse
from rest_framework.permissions import AllowAny



# Create your views here.    

@api_view(["GET", "POST"])
def reviewList(request, movie_pk):
    if request.method == "GET":
        reviews = Review.objects.filter(movie=movie_pk).order_by('-id')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    
# @login_required

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    reviews = get_object_or_404(Review, pk = review_pk)
    if request.method == "PUT":
        serializer = ReviewSerializer(reviews, data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == "DELETE":
        # 자기 자신의 것만 삭제할 수 있어야한다.
        reviews.delete()
        review_ans = {"delete" : f"review {review_pk} is deleted"}
        return Response(review_ans)
    
    
@api_view(["GET", "POST"])
# @authentication_classes([SessionAuthentication])  # 인증 클래스 설정
@permission_classes([IsAuthenticated])  # 권한 설정
def createReview(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)

    # 지금까지 적힌 모든 review를 다보여주는 로직
    if request.method == "GET":
        reviews = movie.review_set.all()

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    # 적은 리뷰를 DB에 저장하고 JSON형태로 응답하는 로직
    elif request.method == "POST":
        # if request.user.is_authenticated:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=request.user)
            print("save")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 무비리스트를 보내주는 로직
@api_view(["GET"])       
def movie_list(request):
    movies = Movie.objects.all()
    if request.method == "GET":
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 무비의 디테일 요소를 보여주는 로직
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        serialzer = Movie_List_Serializer(movie)
        # print(serialzer.data)
        return Response(serialzer.data, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like.all():
        movie.like.remove(request.user)
    else:
        movie.like.add(request.user)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# 장르 아이디, 이름을 배열로 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def genre_ids(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# 장르 아이디를 받아서 해당 장르의 영화리스트 반환
@api_view(['GET'])
@permission_classes([AllowAny])
def genres(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = genre.movies.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# 영화 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movieLike(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if request.user in movie.like.all():
        movie.like.remove(user)
    else:
        movie.like.add(user)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

