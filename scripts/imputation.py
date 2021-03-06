import pandas as pd
import numpy as np

FILL_VALUE = 0 #-1

def fillMissing(inputcsv, outputcsv):
    
    # read input csv - takes time
    df = pd.read_csv(inputcsv, low_memory=False)
    # Fix date bug
    # df.cf4fint = ((pd.to_datetime(df.cf4fint) - pd.to_datetime('1960-01-01')) / np.timedelta64(1, 'D')).astype(int)
    
    
    # if emplty, replace with 0
    df = df.fillna(value=FILL_VALUE)

    # # replace negative values with 1
    # num = df._get_numeric_data()
    # num[num < 0] = 1

    df = df.astype(int)
    # write filled outputcsv
    df.to_csv(outputcsv, index=False)
    
# Usage:
if __name__=='__main__':
    fillMissing('../data/testX_num.csv', '../data/testX_num_output.csv')
    filleddf = pd.read_csv('../data/testX_num_output.csv', low_memory=False)

    fillMissing('../data/trainX_num.csv', '../data/trainX_num_output.csv')
    filleddf = pd.read_csv('../data/trainX_num_output.csv', low_memory=False)
