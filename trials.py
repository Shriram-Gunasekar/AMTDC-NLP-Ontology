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
    return doc.ents

def alphanum(mylist):
    mylist = catal_order(doc)
    orders = []
    catalogue = []
    x = None
    for i in mylist:
        try:
            x = int(i)
            orders.append(x)
        except:
            catalogue.append(i)
    print(orders,catalogue)

alphanum(catal_order(doc))
            
            
            
            