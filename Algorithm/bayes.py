from sklearn.model_selection import train_test_split # version 0.18.1
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from Algorithm import Model as model


def Bayes(data, target):
    data_test = train_test_split(data, target, train_size=0.8, test_size=0.2)
    data_train, data_test, target_train, target_test = data_test
    #train
    clf = GaussianNB()
    clf.fit(data_train, target_train)
    model.save_Model('Bayes.sav',clf)
    #predict
    result = clf.predict(data_test)
    #score
    return (accuracy_score(result, target_test))

