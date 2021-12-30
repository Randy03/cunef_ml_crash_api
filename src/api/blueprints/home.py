from http import HTTPStatus
from flask import Blueprint
from api.models.home import HomeModel
from api.schemas.home import HomeSchema

app_home = Blueprint('home', __name__)


@app_home.route('/',methods=['GET'])
def home_route():
    result = HomeModel()
    schema = HomeSchema()
    return schema.dumps(result), 200
