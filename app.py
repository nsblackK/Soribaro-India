from flask import Flask,request, url_for, redirect, render_template
import pickle

app = Flask(__name__)

with open('transcribeAndTranslate.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    return render_template("soribaro-india.html")

@app.route('/transcribe',methods=['POST','GET'])
def predict():
    audiofile = request.form['fileInput']
    modelsize = request.form['Model']
    lang = request.form['language2']

    transcription, translation = model(modelsize, audiofile, lang)
    if request.method == "POST":
        return(transcription,translation)
    return render_template('soribaro-india.html')

if __name__ == '__main__':
    app.run(debug=True)
