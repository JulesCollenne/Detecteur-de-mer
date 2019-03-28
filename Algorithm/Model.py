#import .. .Reader as re
import pickle
from sklearn.metrics import accuracy_score
import os

import sys
sys.path.insert(0,'..')
import Reader as re
sys.path.insert(0,'')

folder = 'output_Model'

def load_Model(f,data):
    loadeded_model=pickle.load(open(folder+'/'+f,'rb'))
    result=loadeded_model.predict(data)
    return result
    
def save_Model(filename,model):
    os.makedirs(folder, exist_ok=True)
    pickle.dump(model,open(folder+'/'+filename,'wb'))

def simple_load(model_path):
    model = pickle.load(open(model_path,'rb'))
    
    return model

