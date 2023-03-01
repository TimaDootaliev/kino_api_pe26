from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres

@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

create_genre('Детектив')
create_genre('Ужасы')
# delete_genre('Детектив')
print(get_genres())
