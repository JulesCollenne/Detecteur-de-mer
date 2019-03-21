from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from Algorithm import Model as model

def ada_boost(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)
    clf = AdaBoostClassifier()
    clf.fit(X_train, y_train)
    model.save_Model('AdaBoost.sav',clf)
    y_predits = clf.predict(X_test)
    
    return accuracy_score(y_test, y_predits)
