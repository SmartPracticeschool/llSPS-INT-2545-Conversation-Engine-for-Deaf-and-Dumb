import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
global graph
graph = tf.get_default_graph()
from flask import Flask , request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
model = load_model("D:\Flask app\pred.h5")

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        
        img = image.load_img(filepath,target_size = (128,128))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis =0)
        
        with graph.as_default():
            preds = model.predict_classes(x)
            print("prediction",preds)

        index = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        if(str(index[preds[0]])=="0"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="1"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="2"):
        	text = "the predicted Alphabet or number  is : "+ str(index[preds[0]])   	
        elif(str(index[preds[0]])=="3"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])  
        elif(str(index[preds[0]])=="4"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])  
        elif(str(index[preds[0]])=="5"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="6"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])  
        elif(str(index[preds[0]])=="7"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="8"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])  
        elif(str(index[preds[0]])=="9"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])   	
        elif(str(index[preds[0]])=="A"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="B"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="C"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="D"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="E"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="F"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="G"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="H"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="I"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="J"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="K"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="L"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="M"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="N"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="O"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="P"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="Q"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]]) 
        elif(str(index[preds[0]])=="R"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="S"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="T"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="U"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="V"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="W"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="X"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="Y"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        elif(str(index[preds[0]])=="Z"):
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
        else:
        	text = "the predicted Alphabet or number is : " + str(index[preds[0]])
            


    return text
if __name__ == '__main__':
    app.run(debug = True, threaded = False)
        
        
        
    
    
    
