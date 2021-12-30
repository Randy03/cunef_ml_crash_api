from marshmallow import Schema, post_load
from marshmallow.fields import Str
from api.models.home import HomeModel


class HomeSchema(Schema):
    message = Str()

    @post_load
    def make_home(self, data, **kwargs):
        return HomeModel(**data)