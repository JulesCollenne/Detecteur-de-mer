from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier
from Algorithm import Model as model


def ada_boost_train(img, target):
    
    clf = AdaBoostClassifier()
    clf.fit(img, target)
    model.save_Model('AdaBoost_cross.sav',clf)

    return clf


def ada_boost_predict(img, target, clf):

    predits = clf.predict(img)
    
    return accuracy_score(target, predits)