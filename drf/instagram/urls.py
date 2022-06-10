from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)
# 이렇게 하면 2개의 url을 만들어서 router.urls에 리스트 형태로 저장해놓음

urlpatterns = [
    path('', include(router.urls)),  # url 매핑까지 간단하게 할 수 있음
    # path('public/', views.public_post_list),
]
