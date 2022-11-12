from flask import Flask, render_template,request
import score as s
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
    score_pred = 0.0
    mk = 0.0
    if request.method=='POST':
        text1=request.form['text1']
        text2=request.form['text2']
        score_pred=s.semantic_score(text1,text2)
        mk=score_pred
    return render_template("index.html",my_score=mk)

if __name__ == '__main__':
    app.run(debug = 'True')