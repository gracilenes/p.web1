from flask import *
app = Flask(__name__)
convidados = ["Gracilene"]
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/verificar", methods=['POST'])
def verificar_convidado():
    nome = request.form.get("nomeusuario")
    if(nome in convidados):
        msg = "Você está convidado"
        return render_template("resultado.html", msg=msg)
    else:
        msg = "você não está convidado"
        return render_template("resultado.html", msg=msg)
    

if __name__ == '__main__':
    app.run(debug=True)