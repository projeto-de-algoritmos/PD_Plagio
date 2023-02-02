from flask import Flask, render_template, request, flash

app = Flask(__name__)

from controller.texto import TextoController

controller = TextoController()

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        str1 = str(request.form.get('str1'))
        str2 = str(request.form.get('str2'))

        if not str1:
            flash('Ambos textos são necessarios')
        elif not str2:
            flash('Ambos textos são necessarios')
        else:
            return render_template('base.html', compara_str=controller.compara_str(str1, str2),str1=str1, str2=str2)
    else:
        return render_template('base.html', str1='', str2='')
