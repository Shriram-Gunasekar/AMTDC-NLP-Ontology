#trials

import spacy
import en_core_web_md
#Initialized Model
nlp = spacy.load('en_core_web_md')
doc = nlp('Give me a tool with steel material and ')

sent1 = nlp('material of grade')
sent2 = nlp('tool of grade')
print(sent1.similarity(sent2))