import json 
import pandas as pd
f = pd.read_excel(r"Insert_Geometry.xlsx") 
df = f.to_json(orient='records')
with open('E:\\Work\\AMTDC\\Project\\Cypher\\Insert_Geometry.json', 'w') as outfile:
    json.dump(df, outfile)