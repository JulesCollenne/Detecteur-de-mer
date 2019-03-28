from sklearn.model_selection import train_test_split # version 0.18.1
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score






from Algorithm import Model as model



def Bayes(X_train, X_test, y_train, y_test):
    #train
    clf = GaussianNB()
    clf.fit(X_train,y_train)
    model.save_Model('Bayes.sav',clf)
    #predict
    result = clf.predict(X_test)
    #score
    #return (accuracy_score(result, y_test))
    return result

