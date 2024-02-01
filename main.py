from flask import *
from forms import UserForm
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumno",methods=['GET','POST'])
def alumno():
    alumno_clase = UserForm(request.form)
    nombre=''
    apaterno=''
    amaterno=''
    numeroCelular=''
    if request.method == "POST":
       nombre=alumno_clase.nombre.data
       apaterno=alumno_clase.apaterno.data
       amaterno=alumno_clase.amaterno.data
       numeroCelular=alumno_clase.numeroCelular
       
       print("Nombre: {}, Apellido Paterno: {}, Apellido Materno: {}, NumeroCeular: {}".format(nombre,apaterno,amaterno,numeroCelular))

    return render_template("alumno.html",form=alumno_clase,nombre=nombre,apaterno=apaterno,amaterno=amaterno,numeroCelular=numeroCelular)

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


@app.route("/calcular",methods=["GET","POST"])
def calcular():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        return "la Mulrtiplacion de {} x {} es: {}".format(n1,n2,str(int(n1)*int(n2)))
    else:

        return '''
    <form action="/calcular" method="POST">
        <label>N1:</label>
        <input type="text" name="n1"><br>
        <label>N2:</label>
        <input type="text" name="n2"><br>
        <input type="submit"/>

    </form>
'''

@app.route("/operasBAs")
def operas():
    return render_template("operasBas.html")
@app.route("/resultado",methods=["GET","POST"])
def resultado():
     if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        return "la Mulrtiplacion de {} x {} es: {}".format(n1,n2,str(int(n1)*int(n2)))
if __name__=="__main__":
    app.run(debug=True)
    
