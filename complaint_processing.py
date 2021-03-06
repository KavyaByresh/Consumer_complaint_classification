# -*- coding: utf-8 -*-
"""
Project: XYZ logistic consumer complaints management
Created by: Kavya A
Date created : 01-dec-2020
Purpose:
This is a sample web based online consume complaint registering and tracking module
Features:
1. Online submission of consumer complaints
2. Storing the complaints data in SQLite database
3. Tracking  the complaints to appropriate department using a machine learning model

"""

from flask import Flask, render_template, request
from flask_cors import CORS
from model import writing_data,complaint_status
import pickle

complaints_class = pickle.load(open("complaint_classify_model.pickle", 'rb'))
print(complaints_class)

# REST API service
app = Flask(__name__)
CORS(app)

#API to rendering home page
@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template('main.html')


# Build API for calling complaint registering model
@app.route('/register.html',methods=['POST', 'GET'])
def complaints_submission():
    message = ''
    dname=" "
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        try:
            cname = request.form.get('cname')
            inum = request.form.get('inum')
            idate = request.form.get('idate')
            pname = request.form.get('pname')
            complaint = request.form.get('complaint')
            print('your complaintis been submitted sucessfully!!!!')
            ref_no = writing_data(cname,inum,idate,pname,complaint)
            print(ref_no)
            print(complaint)
            dname=complaints_class.predict([complaint])
            print(dname)
            message = 'Your complaint is assigned to : '+str(dname),'department and reference number is : '+str(ref_no)
        except:
            message = 'Error!'   
    return render_template('register.html',reference_num = message)

#Build  API for calling complaint tracking model
@app.route('/track.html',methods=['POST', 'GET'])
def complaint_track():
    message = ""
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        try:
            ref_no = request.form.get('ref_num')
            print(ref_no)
            status=complaint_status(ref_no)
            print(status)
            print("search sucessful")
            message = 'Your complaint is : '+str(status)

        except:
            message = 'Error!'   
    return render_template('track.html', complaint_status=message)
    

 # start the web service
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80)           