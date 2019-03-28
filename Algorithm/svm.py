from sklearn.metrics import accuracy_score
from sklearn import svm
from Algorithm import Model as model

def svmModel(X_train, X_test, y_train, y_test):
    
    clf = svm.SVC(kernel='linear', C=10.,shrinking=False)
    clf.fit(X_train, y_train)
    model.save_Model('svm.sav',clf)
    y_predict = clf.predict(X_test)
    
    #return accuracy_score(y_test, y_predict)
    return y_predict