from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_film_with_genres
from app.schemas.posts import PostShow

@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

# create_genre('Детектив')
# create_genre('Ужасы')
# delete_genre('Детектив')
# print(get_genres())
# create_post('Вторая жизнь Уве', 'Best Film', '2015', 'Sweden', ['Детектив', 'Ужасы'])
a = PostShow.from_orm(get_film_with_genres(5))
for i in a.genre:
    print(i.title)