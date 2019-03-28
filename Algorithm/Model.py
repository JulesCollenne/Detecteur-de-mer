#import .. .Reader as re
import pickle
from sklearn.metrics import accuracy_score
import os

import sys
sys.path.insert(0,'..')
import Reader as re
sys.path.insert(0,'')

folder = 'output_Model'

def load_Model(f, pathPredict):
    data,target =re.dataHistogramme(pathPredict)
    loadeded_model=pickle.load(open(folder+'/'+f,'rb'))
    result=loadeded_model.predict(data)
    return(accuracy_score(result, target))
    
def save_Model(filename,model):
    os.makedirs(folder, exist_ok=True)
    pickle.dump(model,open(folder+'/'+filename,'wb'))