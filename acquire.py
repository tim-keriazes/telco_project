#from acquire import *

import pandas as pd
import numpy as np
import os
from env import host, user, password

#function uses info from env.py file to create a connection url to access db

def get_connection(db, user=user, host=host, password=password):
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

##reads in telco data from db, writed data to csv in no local file exists, returns a df
def get_telco_data():
    
    if os.path.isfile('telco.csv'):
        #if csv exists read in data
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        #read in fresh data from db to df
        df = new_telco_data()
        #cache data
        df.to_csv('telco.csv')
        
    return df
