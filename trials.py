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

def analyze():
    
    