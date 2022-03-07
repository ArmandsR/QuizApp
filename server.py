from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/test')
parametri = ["Augums","Svars","Vecums"]
def health():
  return render_template("test.html",param=parametri)

if __name__ == '__main__':
  app.run(debug="true")
