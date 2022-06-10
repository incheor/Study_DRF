# render는 안 씀
# from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


# def post_list(request):
#     최소 2개 분기
#     list 기능, create 기능
#     pass

# def post_detail(request):
#     최소 3개 분기
#     get 기능, update 기능, delete 기능
#     pass

# generics 활용 PublicPostListAPIView 구현
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# APIView 활용 PublicPostListAPIView 구현
# # generics을 사용하지 않고 APIView를 통해 위처럼 기능하는 조회 구현
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
# 
# 
# public_post_list = PublicPostListAPIView.as_view()

# 함수 기반 뷰로 PublicPostListAPIView 구현
# @api_view(['GET'])
# def public_post_list(request):
#     # 아래 3줄은 위 APIView 복붙
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    # 위 5개 분기를 아래 두 정보만으로 다 처리할 수 있음
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 공개된 포스트 목록 조회
    @action(detail=False, methods=['GET'])
    def public(self, request):
        # qs = self.queryset.filter(is_public=True)
        qs = self.get_queryset().filter(is_public=True)
        # serializer = PostSerializer(qs, many=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # 특정 필드값 변경
    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        # instance.save()를 하면 전체 DB가 업데이트 됨
        # 특정 필드만 업데이트 해보자
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
