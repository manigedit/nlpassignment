
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

import text



features_train , features_test, labels_train, labels_test  = cross_validation.train_test_split(text.preload(), text.get_label(), test_size = 0.2, random_state = 50)


vectorizer = TfidfVectorizer(sublinear_tf = True, min_df=0.3, stop_words='english')
features_train_transformed = vectorizer.fit_transform(features_train)
features_test_transformed = vectorizer.transform(features_test)



selector = SelectPercentile(f_classif, percentile = 1)
selector.fit(features_train_transformed, labels_train)
features_train_transformed = selector.transform(features_train_transformed).toarray()
features_test_transformed = selector.transform(features_test_transformed).toarray()

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()
clf.fit(features_train_transformed,labels_train)

prd = clf.predict(features_test_transformed)

accuraccy = accuracy_score(labels_test, prd)

print("Accuracy is ",accuraccy)
