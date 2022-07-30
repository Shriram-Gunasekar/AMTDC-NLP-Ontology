import re
from difflib import SequenceMatcher
import spacy
import en_core_web_md
nlp = spacy.load('en_core_web_md')

def query():
    query = input("Enter your query: ")
    return query

query = query()
query = query.lower()
doc = nlp(query) 

#L = []
#for token in doc:
#    L.append((token.text,token.pos_))
#for tup in L:
#    if tup[0] == '-':
#        L.pop(L.index(tup)-1)
#        L.remove(L[L.index(tup)+1])
#        L.remove(tup)
#print(L)

def similar(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def catal_order(doc):
    L = []
    for token in doc:
        if token.is_oov:
          L.append(token)
    return L
    
def ner(doc):
    L = []
    for ent in doc.ents:
        L.append(ent.text)
    return L

    