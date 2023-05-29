from django.urls import path
from . import views
urlpatterns = [
    # path('MovieCreate/', views.MovieCreate), #장고 DB에 남기기 위한 코드
    path('ServerToClient/', views.movie_list),  # 무비 리스트
    path('MovieDetail/<int:movie_pk>/', views.movie_detail), # 무비 디테일
    path('MovieDetail/<int:movie_pk>/reviews/', views.createReview), # 리뷰 생성 및 삭제
    path('reviews/<int:movie_pk>/', views.reviewList), # 무비리스트에 해당하는 리뷰만 가져오는
    path('reviewDelete/<int:review_pk>/', views.review_update_delete), # 리뷰를 삭제 및 수정
    path('like/<int:movie_pk>/', views.movieLike),
    path('genres/ids/', views.genre_ids),
    path('genres/<int:genre_id>/', views.genres)
    # path('MovieDetail/<int:movie_pk>/', views.movie_detail), # 무비 디테일
]
