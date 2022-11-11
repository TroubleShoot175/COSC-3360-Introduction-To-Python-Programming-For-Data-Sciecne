''' Homework 08 - Exercise 02 '''

import pandas as pd
from titles import strToTitle

def dfDescribe(df):
    
    
    
    print(strToTitle("Built Describe"))
    
    

grades_dict = {'Wally' : [87, 96, 70], 'Eva' : [100, 87, 90], 
              'Sam' : [94, 77, 90], 'Katie' : [100, 81, 82], 
              'Bob' : [83, 65, 85]}

df = pd.DataFrame(grades_dict)

dfDescribe(df)
