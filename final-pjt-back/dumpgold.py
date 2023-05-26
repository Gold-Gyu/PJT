import os
import sys
import django
import json
from django.conf import settings
from movies.models import Genre, Movie

# Django 프로젝트의 루트 디렉토리 경로로 변경해주세요.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django 프로젝트의 settings.py 모듈을 임포트하기 위한 설정
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# Django 초기화
django.setup()

def dump_genres_movies():
    genres_movies = Movie.genre_ids.through.objects.all()
    genre_movie_list = []
    for genre_movie in genres_movies:
        genre_movie_data = {
            'model': 'movies.genres_movies',
            'pk': genre_movie.pk,
            'fields': {
                'genre_id': genre_movie.genre_id,
                'movie_id': genre_movie.movie_id,
            }
        }
        genre_movie_list.append(genre_movie_data)

    with open('genres_movies.json', 'w', encoding='utf-8') as f:
        json.dump(genre_movie_list, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # Django 설정 로드
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    django.setup()

    dump_genres_movies()
