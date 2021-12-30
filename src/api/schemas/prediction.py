from marshmallow import Schema, post_load
from marshmallow.fields import Str, Number, validate,Float, Integer
from api.models.prediction import PredictionInputModel, PredictionOutputModel


class PredictionInputSchema(Schema):
    C_MNTH = Str(default=None,validate=validate.OneOf(['01','02','03','04','05','06','07','08','09','10','11','12']))
    C_WDAY = Str(default=None,validate=validate.OneOf(['1','2','3','4','5','6','7']))
    C_HOUR = Str(default=None,validate=validate.OneOf(['1','2','3','0']))
    C_VEHS = Number(default=None)
    C_CONF = Str(default=None,validate=validate.OneOf(['34','01','42','04','31','21','23','03','02','33','24','35','41','06','32','36','05','22','25']))
    C_RCFG = Str(default=None,validate=validate.OneOf(['13','01','02','03','05','04','06','08','07','09','10']))
    C_WTHR = Str(default=None,validate=validate.OneOf(['1','5','3','4','7','2','6','8']))
    C_RSUR = Str(default=None,validate=validate.OneOf(['5','3','2','4','1','6','10','7','9','8']))
    C_RALN = Str(default=None,validate=validate.OneOf(['3','6','1','2','5','4','7']))
    C_TRAF = Str(default=None,validate=validate.OneOf(['03','18','01','06','10','05','04','11','19','07','08','16','17','02','13','15','09','12']))
    V_TYPE = Str(default=None,validate=validate.OneOf(['06','01','11','20','17','07','08','24','09','22','14','23','05','16','18','19','10','21']))
    P_SEX = Str(default=None,validate=validate.OneOf(['F','M']))
    P_AGE = Number(default=None)
    P_SAFE = Str(default=None,validate=validate.OneOf(['02','01','13','12','09','14','10','11']))
    C_PERS = Number(default=None)
    V_AGE = Number(default=None)

    @post_load
    def make_prediction_input(self, data, **kwargs):
        return PredictionInputModel(**data)

class PredictionOutputSchema(Schema):
    label = Integer(required=True,validate=validate.OneOf([0,1]))
    prob0 = Float(required=True,validate=validate.Range(min=0, max=1))
    prob1 = Float(required=True,validate=validate.Range(min=0, max=1))

    @post_load
    def make_prediction_putput(self, data, **kwargs):
        return PredictionOutputModel(**data)
