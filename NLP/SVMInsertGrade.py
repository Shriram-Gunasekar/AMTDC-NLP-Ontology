import json
with open('InsertGradeData.json','r') as f:
        data = json.load(f)
        
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(binary=True)
train_annot = vectorizer.fit_transform(data['Descriptions'])

#print(vectorizer.get_feature_names_out())
#print(vectors.toarray())

from sklearn import svm
clf_svm = svm.SVC(kernel='linear')
clf_svm.fit(train_annot,data['Grades'])

test_x = vectorizer.transform(['Lightweight, easy to use, and very comfortable.'])
print(clf_svm.predict(test_x))