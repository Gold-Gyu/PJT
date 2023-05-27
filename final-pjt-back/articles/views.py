
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, CommentSerializer
from .models import Article, Comment
# from .forms import CommentForm

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create(request):

    # pk값 내림차순으로 정렬하는 로직
    if request.method == 'GET':
        articles = get_list_or_404(Article.objects.order_by('-id'))
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시글을 생성하는 로직
    elif request.method == 'POST':
        serializer = ArticleListSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail(request, article_pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def update_delete(request, article_pk):

    articles = get_object_or_404(Article, pk=article_pk)
    if request.method == "PUT":
        serializer = ArticleListSerializer(articles, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        articles.delete()
        review_ans = {"delete" : f"review {article_pk} is deleted"}
        return Response(review_ans, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    elif request.method =="GET":
        comment = Comment.objects.filter(article=article)

        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_delete_upadate(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user_id != request.user.id:
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'DELETE':
        comment.delete()
        return Response({'id':comment_pk}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def like(request, article_pk):
#     review = get_object_or_404(Article, pk=article_pk)
#     if request.user in review.like.all():
#         review.like.remove(request.user)
#     else:
#         review.like.add(request.user)
#     serializer = ReviewSerializer(review)
#     return Response(serializer.data)
    