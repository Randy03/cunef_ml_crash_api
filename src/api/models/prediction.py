class PredictionInputModel():
    def __init__(self,C_MNTH=None,C_WDAY=None,C_HOUR=None,C_VEHS=None,C_CONF=None,
    C_RCFG=None,C_WTHR=None,C_RSUR=None,C_RALN=None,C_TRAF=None,V_TYPE=None,
    P_SEX=None,P_AGE=None,P_SAFE=None,C_PERS=None,V_AGE=None):
        self.C_MNTH = C_MNTH
        self.C_WDAY = C_WDAY
        self.C_HOUR = C_HOUR
        self.C_VEHS = C_VEHS
        self.C_CONF = C_CONF
        self.C_RCFG = C_RCFG
        self.C_WTHR = C_WTHR
        self.C_RSUR = C_RSUR
        self.C_RALN = C_RALN
        self.C_TRAF = C_TRAF
        self.V_TYPE = V_TYPE
        self.P_SEX  = P_SEX  
        self.P_AGE  = P_AGE  
        self.P_SAFE = P_SAFE
        self.C_PERS = C_PERS
        self.V_AGE  = V_AGE  


class PredictionOutputModel():
    def __init__(self,label,prob0,prob1):
        self.label = label
        self.prob0 = prob0
        self.prob1 = prob1