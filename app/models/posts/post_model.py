import peewee as pw

from app.models.basemodel import AbstractModel


class GenreModel(AbstractModel):
    title = pw.CharField(100)


class PostModel(AbstractModel):
    title = pw.CharField(100)
    description = pw.TextField(null=True)
    year = pw.DateField()
    country = pw.CharField(100)
    genre = pw.ManyToManyField(GenreModel, backref='films')


GenrePosts = PostModel.genre.through_model

# class GenrePosts():
#     post_id = pw.ForeignKeyField(PostModel)
#     genre_id = pw.ForeignKeyField(GenreModel)

