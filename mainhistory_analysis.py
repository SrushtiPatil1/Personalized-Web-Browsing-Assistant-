import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('history_analysis.csv')
print(df)

#df = int(df)

profile = ProfileReport(df)
profile.to_file(output_file="history_analysis.html")






