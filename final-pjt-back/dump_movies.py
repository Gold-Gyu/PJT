import os
import sys
import django

# Django 프로젝트의 루트 디렉토리 경로로 변경해주세요.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django 프로젝트의 settings.py 모듈을 임포트하기 위한 설정
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# Django 초기화
django.setup()

import json
from movies.models import Movie

def dump_movies():
    movies = Movie.objects.all()
    movie_list = []
    for movie in movies:
        movie_data = {
            'model': 'movies.movie',  # 앱이름.모델이름 형식으로 지정
            'pk': movie.pk,
            'fields': {
                'title': movie.title,
                'overview': movie.overview,
                'release_date': str(movie.release_date),
                'poster_path': movie.poster_path,
                'popularity': movie.popularity,
                'vote_average': movie.vote_average,

            }
        }
        movie_list.append(movie_data)

    with open('movies.json', 'w', encoding='utf-8') as f:
        json.dump(movie_list, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    dump_movies()