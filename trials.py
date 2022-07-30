#trials

import spacy
import en_core_web_md
from data import Holder, Insert, getquery
#Initialized Model
nlp = spacy.load('en_core_web_md')
doc = nlp(getquery)

##sent1 = nlp('material of grade')
##sent2 = nlp('tool of grade')
##print(sent1.similarity(sent2))

class Similarity:
    material = ["of material", "having material","having material of", "of material of", "of material having"]
    coating = ["of coating", "having coating", "having coating of", "of coating of", "of coating having"]
    catalog = ["catalog number KM50TSMDJNR1506"," catalog number DNMG150604MS","DNMG150604MS","KM50TSMDJNR1506"]
    name = ["M-Clamping","Boring bar","Welding Bar","Threading Holder"]

catalog = ["catalog number KM50TSMDJNR1506"," catalog number DNMG150604MS","DNMG150604MS","KM50TSMDJNR1506"]
for i in range(len(catalog)):
    for j in range(len(catalog)):
        if i != j:
            print(catalog[i], catalog[j])
            print(doc[i].similarity(doc[j]))
            print("\n")
