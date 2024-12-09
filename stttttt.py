import numpy as np
import pickle
loaded_model=pickle.load(open('trained_model.sav','rb'))
imput=([[5,166,72,29,175,25.8,0.587,51]])
pred=loaded_model.predict(imput)
if pred[0]==0:
                print('the person not dibetc')
else:
                print('person is dibetic')