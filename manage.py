from flask import Flask, render_template, request

import random

app = Flask(__name__)


def generation_terme_developpeur():
    deg = random.choice(['1', 'X', 'X**2'])
    terme = random.choice(['-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9'])
    terme_dev = ''
    terme_dev += terme
    terme_dev += '*'
    terme_dev += deg
    return terme_dev


def generation_terme_developpe(nb_termes):
    terme = ''
    for k in range(nb_termes):
        x = generation_terme_developpeur()
        terme += x
    return terme


def verification(c, n):
    X = n
    return eval(c)


def transfo(c):
    c1 = c.replace('(', '*(')
    c2 = c1.replace('X', '*X')
    c3 = c2.replace('^', '**')
    return c3


def deg_transfo(c):
    cf = c.replace('^', '**')
    return cf


@app.route('/')
def index():
    chaine = generation_terme_developpeur()
    chaine += '*('
    chaine += generation_terme_developpe(2)
    chaine += ')'
    chaine1 = chaine.replace('**2', '^2')
    chaine2 = chaine1.replace('*1', '')
    chaine3 = chaine2.replace('*', '')
    return render_template('index.html', subject=chaine3)


@app.route('/developpement', methods=['GET', 'POST'])
def index_developpent():
    global evaluation
    student_result_ = request.form['student_result']
    subject_ = request.form['subject']
    student_result_final = transfo(student_result_)
    subject_final = transfo(subject_)
    result = True
    for i in range(11):
        if verification(student_result_final, i) != verification(subject_final, i):
            result = False
            break
    if not result:
        evaluation = 'faux'
    else:
        evaluation = 'correct'
    return render_template('page_resultat.html', reponse=student_result_, resultat=evaluation)


@app.route('/hello')
def hello_world():
    a = "toto"
    b = a.replace('t', 'c')
    return "Hello world {}!".format(b)


if __name__ == "__main__":
    app.run()
