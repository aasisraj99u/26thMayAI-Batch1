from flask import Flask,render_template,request
import pandas as pd


path = r'/home/abhijain/mysite/TourPackagePredictor.pkl'

model = pd.read_pickle(path)


app = Flask(__name__)

@app.route('/')
def indexpage():
    msg=''
    flag=0
    tag=''
    return render_template('index.html',result=[msg,flag,tag])


@app.route('/predict', methods=['GET','POST'])
def predict():

    if request.method == 'POST':
        flag=1
        MonthlyIncome = request.form['MonthlyIncome']
        Age = request.form['Age']
        DurOfPitch = request.form['DurOfPitch']
        NoOfTrips = request.form['NoOfTrips']

        query = pd.DataFrame({
            'MonthlyIncome':[MonthlyIncome],
            'Age':[Age],
            'DurationOfPitch':[DurOfPitch],
            'NumberOfTrips': [NoOfTrips]
        })
        try:
            if (model.predict(query)[0]==1):
                msg = 'Status: Interested'
                tag= 'success'
            else:
                msg = 'Status: Not Interested'
                tag= 'danger'
        except:
            msg = 'Error: Enter details Correctly !!'
            tag = 'danger'
        #res=[msg,tag]
    return render_template('index.html',result=[msg,flag,tag])

if '__name__' == '__main__':
    app.run(debug = True)