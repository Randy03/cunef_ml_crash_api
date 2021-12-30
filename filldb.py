import pandas as pd
import requests
from sklearn.utils import resample

target = 'C_SEV'


if target == 'C_SEV':
    numeric_features = ['C_VEHS', 'V_AGE','P_AGE','C_PERS']
    categorical_features = ['C_MNTH','C_WDAY','C_HOUR','C_CONF','C_RCFG','C_WTHR','C_RSUR','C_RALN','C_TRAF','P_SEX','P_SAFE','V_TYPE']
    file = 'crash_transformed_c_sev.csv'
    one_hot_categories = ['C_MNTH', 'C_WDAY', 'C_HOUR', 'P_SEX']
    target_categories = ['C_CONF', 'C_RCFG', 'C_WTHR','C_RSUR','C_RALN','C_TRAF','V_TYPE','P_SAFE']
else:
    target = 'P_ISEV'
    numeric_features = ['C_VEHS', 'V_AGE','P_AGE']
    categorical_features = ['C_MNTH','C_WDAY','C_HOUR','C_CONF','C_RCFG','C_WTHR','C_RSUR','C_RALN','C_TRAF','P_SEX','P_PSN','P_SAFE','P_USER','V_TYPE']
    file = 'crash_transformed_p_isev.csv'
    one_hot_categories = ['C_MNTH', 'C_WDAY', 'C_HOUR', 'P_SEX']
    target_categories = ['C_CONF', 'C_RCFG', 'C_WTHR','C_RSUR','C_RALN','C_TRAF','V_TYPE','P_SAFE','P_PSN','P_USER']

dtypes = {}
for feature in numeric_features:
    dtypes[feature] = 'float'
for feature in categorical_features:
    dtypes[feature] = 'str'

#data = pd.read_csv('crash_transformed.csv',dtype=dtypes)
data = pd.read_csv(f'./{file}',dtype=dtypes)

X = data.drop(target,axis=1)
y = data[target]

def subsample_data(X,y):
    y_2 = resample(y[y==0], replace = True, n_samples = len(y[y==1]), random_state = 12345)
    y_resampled = pd.concat([y[y==1],y_2])
    data_resampled = X.join(y_resampled)
    data_resampled = data_resampled.dropna(subset=[y.name])
    _y = data_resampled[y.name].astype('int8')
    _x = data_resampled.drop(target,axis=1)
    return _x,_y

X ,y = subsample_data(X,y)

for i in range(200):
    sample = X.sample(1).values[0]
    params = {
    "C_MNTH":sample[0],
    "C_WDAY":sample[1],
    "C_HOUR":sample[2],
    "C_VEHS":sample[3],
    "C_CONF":sample[4],
    "C_RCFG":sample[5],
    "C_WTHR":sample[6],
    "C_RSUR":sample[7],
    "C_RALN":sample[8],
    "C_TRAF":sample[9],
    "V_TYPE":sample[10],
    "P_SEX":sample[11],
    "P_AGE":sample[12],
    "P_SAFE":sample[13],
    "C_PERS":sample[14],
    "V_AGE":sample[15],
    }
    requests.get("http://172.17.0.10:5000/api/predict", params=params)