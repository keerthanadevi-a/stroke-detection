from flask import Flask, render_template,request
import numpy as np
import pickle

#creating constructor
app=Flask(__name__, template_folder='template',static_folder='static')
model=pickle.load(open('./model/model.pickle', 'rb'))
# print(model)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''v1 = request.form['gender']
    v2 = request.form['age']
    v3 = request.form['hypertension']
    v4 = request.form['heart_disease']
    v5 = request.form['ever_married']
    v6 = request.form['work_type']
    v7 = request.form['residence_type']
    v8 = request.form['avg_glucose_level']
    v9 = request.form['bmi']'''

    features = [float(x) for x in request.form.values()]
    final_feature = [np.array(features)]
    pred = model.predict(final_feature)

    out = pred

    
    if int(out)== 1:
        predi ='You have stroke. Please consult a neurologist!'
    else:
        predi ="You don't have stroke."           
    return render_template("ans.html", prediction = predi)



if __name__ == '__main__':
    app.run(debug=True)