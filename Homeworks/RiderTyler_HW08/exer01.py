''' Homeowrk 08 - Exercise 01 '''

import pandas as pd
from titles import strToTitle

temps ={"Mon": [68, 89], "Tue": [71, 93], "Wed": [66, 82], "Thu": [75, 97], "Fri": [62, 79]}

df = pd.DataFrame(temps, index=["Low", "High"])

strToTitle("Data Frame", True, 'f', True)
print(df)

li = df.loc[ : , "Mon" : "Wed"]

strToTitle("Mon - Wed Columns", True, 'f', True)
print(li)

li = df.loc["Low", : ]

strToTitle("Low Temperatures For Each Day", True, 'h', True)
print(li)

pd.set_option('display.precision', 2)

strToTitle("Average Temperature For Each Day", True, 'h', True)
print(df.mean())

strToTitle("Average Low and High Tempuratures", True, ('c', 10), True)
print(f'Average Low: {df.mean(axis=1)[0]}')
print(f'Average High: {df.mean(axis=1)[1]}')
