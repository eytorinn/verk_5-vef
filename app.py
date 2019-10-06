import os
from flask import Flask, render_template, session, url_for, request, redirect, escape
app = Flask(__name__)

app.secret_key = os.urandom(8)
print(os.urandom(8))

#database
vorur = [   [0, "Peysa", "peysa.jpg", 14000],
            [1, "Skór", "skor.jpg", 26000],
            [2,"Buxur", "buxur.jpg", 10000],
            [3,"Trefill", "trefill.jpg", 200000],
            [4,"Jakki", "jakki.jpg", 7000],
            [5,"Húfa", "hufa.jpg", 3000]
        ]

#rót
@app.route("/")
def index():
    karfa = []
    fjoldi=0
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
    return render_template('index.tpl', v=vorur, fjoldi=fjoldi)

#bætum vöru í körfu
@app.route("/add/<int:id>")
def frett(id):
    karfa = []
    fjoldi = 0
    if 'karfa' in session:
        karfa = session['karfa']
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    #ef karfan er 0
    else:
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    return  render_template('index.tpl',vorur = vorur, fjoldi= fjoldi)
@app.route("/karfa")
def karfa():
    karfa = []
    summa = 0
    # KARFAN ER EKKI TÓM
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)  # fj vara í körfu
        for i in karfa:
            summa += int(i[3])
        return render_template("karfa.tpl", k=karfa, tom=False, fjoldi=fjoldi)
    else:
        return render_template('karfa.tpl', k=karfa, tom=True)

@app.route("/eydavoru/<int:id>")
def eydavoru(id):
    karfa = []
    karfa = session["karfa"]
    vara = 0
    for i in range(len(karfa)):
        if karfa[i][0] == id:
            vara = i
    karfa.remove(karfa[vara])
    session['karfa'] = karfa
    return render_template('eydavoru.tpl')

@app.route('/eyda')
def eyda():
    session.pop('karfa',None)
    render_template('eyda.tpl')

@app.route("/result", methods = ["POST"])
def result():
    if request.method == "POST":
        kwargs={
            'name': request.form['nafn'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'price': request.form['price']

        }
        render_template('result.tpl',kwargs)
        def logout():
            session.pop('karfa', None)
            return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.tpl')

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('method_not_allowed.tpl')


if __name__ == '__main__':
    app.run(debug = True)
