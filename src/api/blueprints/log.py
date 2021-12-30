from flask import Blueprint, json,request,current_app
import pandas as pd
from sqlalchemy import create_engine, DateTime, String,SmallInteger,Text
from datetime import datetime

log = Blueprint('log',__name__)

@log.after_app_request
def log_request(response):
    req = dict(request.args)
    log_dict = {
        "timestamp": [pd.to_datetime(datetime.now())],
        "method": [request.method],
        "path": [request.path],
        "status" : [response.status_code],
        "request" : [None if not req else json.dumps(req)],
        "response": [response.data.decode('utf-8')]
    }
    dtype_dict = {
        "timestamp": DateTime,
        "method": String,
        "path": String,
        "status" : SmallInteger,
        "request" : Text,
        "response": Text
    }
    data = pd.DataFrame(log_dict)
    print(log_dict,flush=True)
    engine = create_engine(current_app.config['SQL_ENGINE'])
    data.to_sql('requests',engine,if_exists='append',index=False,dtype=dtype_dict)

    return response
