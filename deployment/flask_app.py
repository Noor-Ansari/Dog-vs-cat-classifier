from flask import Flask , redirect, render_template
from flask import jsonify, request, flash, url_for
from PIL import Image 
import numpy as np
from predict import Predict

model = Predict()

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method =='POST':
        uploaded_file = request.files['image']
        if uploaded_file.filename=='':
            flash('No file selected')
            return redirect(url_for('home'))
        if uploaded_file and allowed_file(uploaded_file.filename):
            image = Image.open(uploaded_file)
            processed_image = model.preprocess_img(image,(224,224))
            prediction = model.model.predict(processed_image).tolist()
            print(prediction)
            dog = prediction[0][0]
            cat = prediction[0][1]
            pred = {
                'dog':dog,
                'cat':cat,
            }
            return render_template('predict.html', pred=pred)
        else:
            return redirect(url_for('home'))         
    else:
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)