from api.models.prediction import PredictionInputModel, PredictionOutputModel
from joblib import load
import pandas as pd

class PredictionService():
    def __init__(self,model):
        self.model = load(model)

    def make_prediction(self,input):
        input_dict = {}
        for key,value in input.__dict__.items():
            input_dict[key] = [value]
        input_df = pd.DataFrame(input_dict)
        pred = self.model.predict(input_df)
        pred_proba = self.model.predict_proba(input_df)[0]

        return PredictionOutputModel(pred[0],pred_proba[0],pred_proba[1])
