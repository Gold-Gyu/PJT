from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import User
from movies.models import Movie, Genre, Review
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404, get_list_or_404

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def userinfo(request, user_pk):
  user = User.objects.get(pk=user_pk)
  serializer = UserSerializer(user)
  return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes({IsAuthenticated})
def delete(request):
  user = User.objects.get(id=request.user.id)
  if user:
    user.delete()
    return Response({"message" : "회원탈퇴가 완료되었습니다."}, status=status.HTTP_200_OK)
  return Response({"message" : "이미 탈퇴한 사용자입니다."}, status=status.HTTP_400_BAD_REQUEST)