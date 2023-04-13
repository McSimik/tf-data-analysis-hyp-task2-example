import pandas as pd
import numpy as np
import statsmodels.stats.weightstats


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    
    return 1-statsmodels.stats.weightstats.ztest(x,y)[1]<0.06
