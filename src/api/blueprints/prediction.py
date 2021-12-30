from http import HTTPStatus
from flask import Blueprint
from api.models.prediction import PredictionInputModel, PredictionOutputModel
from api.schemas.prediction import PredictionInputSchema, PredictionOutputSchema
from api.services.prediction import PredictionService
from flask import request, current_app


app_predict = Blueprint('predict', __name__)


@app_predict.route('/predict',methods=['GET'])
def predict_route():
    schema = PredictionInputSchema()
    input = schema.load(request.args)
    prediction_service = PredictionService(current_app.config['MODEL_PATH'])
    result = prediction_service.make_prediction(input)
    result_schema = PredictionOutputSchema()
    output = result_schema.dumps(result)
    #log_request(request.method,request.path,request.args,output)
    return output, 200

