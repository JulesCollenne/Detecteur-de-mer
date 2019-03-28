from sklearn.model_selection import train_test_split # version 0.18.1
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from Algorithm import Model as model



def Bayes_train(data, target):
    
    clf = GaussianNB()
    clf.fit(data, target)
    model.save_Model('Bayes.sav',clf)

    return clf
    
def Bayes_predict(data, target, clf):

    predits = clf.predict(data)
    
    return (accuracy_score(target, predits))