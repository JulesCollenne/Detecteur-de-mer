from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier

def ada_boost(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    classifier = AdaBoostClassifier()
    classifier.fit(X_train, y_train)
    y_predits = classifier.predict(X_test)
    
    return accuracy_score(y_test, y_predits)