from distutils.log import debug
from flask import Flask,request,jsonify,render_template, redirect, url_for
import sklearn
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


with open(f'model/ExamenLabo.pkl','rb') as f:
	model=load(f)

app=Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET','POST'])
def index ():
	if flask.request.method == 'GET':
		return (flask.render_template_folder(index.html))
	if flask.request.method == 'POST':
		Pregnancies=flask.render_template.form['Pregnancies']
		Glucose=flask.render_template.form['Glucose']
		BloodPressure=flask.render_template.form['BloodPressure']
		SkinThickness=flask.render_template.form['SkinThickness']
		Insulin=flask.render_template.form['Insulin']
		BMI=flask.render_template.form['BMI']
		DiabetesPedigreeFunction=flask.render_template.form['DiabetesPedigreeFunction']
		Age=flask.render_template.form['Age']

		input_variables = pd.DataFrame([[Pregnancies,Glucose,BloodPressure,
			                          SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
									columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
									'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'],
									dtype='float', 
									index=['int'])
   		predictions=model.predict(input_variables)[0]
   		print(predictions)

   		return flask.render_template('index.html', dictionary_input={'Pregnancies':pregnancies,'Glucose':glucose,'BloodPressure':bloodPressure,'SkinThickness':skinThickness,'Insulin':insulin,'BMI':bMI,'DiabetesPedigreeFunction':diabetesPedigreeFunction,'Age':age} 
   									result=predictions)

   if __name__=='__main__':
	app.run(debug=True)