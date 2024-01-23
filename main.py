from flask import *

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumno")
def alumno():
    nombres=["pedro","robaerto","erick","diego"]
    titulo="UTL!!!!!!1"
    return render_template("alumno.html",titulo=titulo,nombres=nombres)

@app.route("/maestro")
def maestro():
    return render_template("maestro.html")

@app.route("/hola")
def hola():
    return "<h1>prueba de pagina</h1>"

@app.route("/saludo")
def saludo():
    return "<h1>aqui... en mi casa</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "Hola: "+nom


@app.route("/edad/<int:edad>")
def edad(edad):
    return "tu edad es: {}".format(edad)


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "la suma de {} + {} es: {}".format(n1,n2,n1+n2)

@app.route("/default")
@app.route("/default/<string:d>")
def fun(d="el cala"):
    return "el nombre del usuario es: "+d 

def edad(edad):
    return "tu edad es: {}".format(edad)




if __name__=="__main__":
    app.run(debug=True)
    
