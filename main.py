from app.models.basemodel import db_connection
from app.models.posts.post_model import GenreModel, PostModel, GenrePosts

db_connection.create_tables([GenreModel, PostModel, GenrePosts])