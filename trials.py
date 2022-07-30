import re
import spacy
import en_core_web_md
from data import Holder, Insert, getquery
nlp = spacy.load('en_core_web_md')


doc = nlp("We need an M-Clamping material of catalog number KM50TSMDJNR1506 catalog number KM50TSMDJNR1506 P-Steel") 
L = []
for token in doc:
    print(token.text,token.pos_)