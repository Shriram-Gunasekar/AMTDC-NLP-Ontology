import json 
import pandas as pd

f = pd.read_excel('Insert_Geometry.xlsx')
NodeName = [i for i in f['property 1']]
property = [i for i in f['property 2']]
D = dict()
for i in range(len(NodeName)):
    D[NodeName[i]] = [property[i]]
with open('Insert_Geometry.json', 'w') as f:
    json.dump(D, f, indent = 2)




