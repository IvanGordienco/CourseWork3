from project.dao.genre import GenreDAO
from project.exceptions import ItemNotFound
from project.schemas.genre import GenreSchema
from project.services.base import BaseService


class GenresService(BaseService):
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        genre = GenreDAO(self._db_session).get_by_id(pk)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all_genres(self):
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)

    def create(self, pk):
        return self.dao.create(pk)

    def update(self, pk):
        self.dao.update(pk)
        return self.dao

    def delete(self, pk):
        self.dao.delete(pk)

