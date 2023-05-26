import requests
import json

idx = 1
ret = []
for page in range(1, 100):
    url = "https://api.themoviedb.org/3/movie/popular?api_key=35d17e16b23f3b0c8910eb439960f992&language=ko-KR&page=" + str(page)
    res = requests.get(url)
    res = res.json()
    movies = res["results"]

    for movie in movies:
        # 포스터가 없는 영화 데이터
        if not movie["poster_path"] or not movie['title'] or not movie['overview'] or not movie['release_date'] or not movie['vote_count'] or not movie['genre_ids']:
            continue
        inner = dict()
        inner['model'] = "movies.movie"
        inner['pk'] = idx
        idx += 1
        temp = dict()
        temp['title'] = movie['title']
        temp['overview'] = movie['overview']
        temp['release_date'] = movie['release_date']
        temp['vote_average'] = movie['vote_average']
        temp['poster_path'] = movie['poster_path']
        # genres = movie['genre_ids']
        # genreIds = ','.join(list(map(str, genres)))
        temp['genres'] = movie['genre_ids']
        inner['fields'] = temp
        ret.append(inner)
	   
    file = open("moviedata.json", "w+")
    file.write(json.dumps(ret))