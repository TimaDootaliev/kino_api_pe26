import peewee as pw

from app.models.basemodel import AbstractModel


class Genre(AbstractModel):
    title = pw.CharField(100, unique=True)


class Post(AbstractModel):
    title = pw.CharField(100)
    description = pw.TextField(null=True)
    year = pw.DateField(formats=['%Y'])
    country = pw.CharField(100)
    genre = pw.ManyToManyField(Genre, backref='films')


PostGenres = Post.genre.through_model
# class PostGenres():
#     post_id = pw.ForeignKeyField(Post)
#     genre_id = pw.ForeignKeyField(Genre)
