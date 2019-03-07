from sklearn.model_selection import train_test_split # version 0.18.1
from sklearn.naive_bayes import GaussianNB

# split the data with 50% in each set
data_test = train_test_split(data, target
                                 , random_state=0
                                 , train_size=0.5)
data_train, data_test, target_train, target_test = data_test

#train
clf = GaussianNB()
clf.fit(data_train, target_train)
#predict
result = clf.predict(data_test)
#score
accuracy_score(result, target_test)