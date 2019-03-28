
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from Algorithm import Model as model

def ada_boost(X_train, X_test, y_train, y_test):
    clf = AdaBoostClassifier(n_estimators=10)
    clf.fit(X_train, y_train)
    model.save_Model('AdaBoost.sav',clf)
    y_predict = clf.predict(X_test)
    
    #return accuracy_score(y_test, y_predict)
    return y_predict
