import os
import sys
import django
import json
from movies.models import Movie, Genre, MovieGenre

# Django 프로젝트의 루트 디렉토리 경로로 변경해주세요.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django 프로젝트의 settings.py 모듈을 임포트하기 위한 설정
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# Django 초기화
django.setup()

def dump_movie_genres():
    movie_genres = Genre.objects.all()
    movie_genre_list = []
    for movie_genre in movie_genres:
        movie_genre_data = {
            'model': 'movies.moviegenre',
            'pk': movie_genre.pk,
            'fields': {
                'movie_id': movie_genre.movie_id,
                'genre_id': movie_genre.genre_id,
            }
        }
        movie_genre_list.append(movie_genre_data)

    with open('movie_genres.json', 'w', encoding='utf-8') as f:
        json.dump(movie_genre_list, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    # Django 설정 로드

    dump_movie_genres()