import re
from difflib import SequenceMatcher
import spacy
import en_core_web_md
from data import *
nlp = spacy.load('en_core_web_md')

doc = nlp("We need an M-Clamping material of catalog number" 
          "KM50TSMDJNR1506 catalog number KM50TSMDJNR1506 P-Steel") 
L = []
for token in doc:
    L.append((token.text,token.pos_))
for tup in L:
    if tup[0] == '-':
        L.pop(L.index(tup)-1)
        L.remove(L[L.index(tup)+1])
        L.remove(tup)
print(L)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    