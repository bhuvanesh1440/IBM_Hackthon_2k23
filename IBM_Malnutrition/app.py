from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/severewasting')
def swasting():
    return render_template('severewasting.html')

@app.route('/overweight')
def overweight():
    return render_template('overweight.html')

@app.route('/underweight')
def underweight():
    return render_template('underweight.html')
@app.route('/stunting')
def stunting():
    return render_template('stunting.html')
@app.route('/wasting')
def wasting():
    return render_template('wasting.html')



if __name__ =='__main__':
     app.run(debug=True, port=5000,host="0.0.0.0")
 