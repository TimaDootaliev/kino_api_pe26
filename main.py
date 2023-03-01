from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id

@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

create_genre('Детектив')
create_genre('Ужасы')
# delete_genre('Детектив')
# print(get_genres())
# create_post(
#     'Ходячие мертвецы', 
#     "Сериал про зомби!",
#     '2003',
#     'USA',
#     ['Детектив', 'Ужасы'])
# create_post(
#     'Шерлок Холмс', 
#     "Сериал про детектива!",
#     '2005',
#     'USA',
#     ['Детектив'])
# print(get_all_films())
print(get_film_by_id(1))