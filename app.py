from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/basededatos.db'
db = SQLAlchemy(app)

class Personal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_del_empleado = db.Column(db.String(50))
    apellido_del_empleado = db.Column(db.String(50))
    nombre_completo_del_empleado = db.Column(db.String(100))
    cedula_de_identidad_del_empleado = db.Column(db.String(50))
    numero_telefonico_asignado = db.Column(db.String(50))
    contraseña_del_empleado = db.Column(db.String(50))
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/", methods=['GET','POST'])
def auth():
    cedula_inicio_sesion = request.form.get("cedula_de_empleado")
    contraseña_inicio_sesion = request.form.get("contraseña_del_empleado")
    usuario_cedula = Personal.query.filter_by(cedula_de_identidad_del_empleado=cedula_inicio_sesion).first()
    usuario_contraseña = Personal.query.filter_by(contraseña_del_empleado=contraseña_inicio_sesion).first()
    if usuario_cedula and usuario_contraseña:
        return render_template('home.html')
    return render_template('auth.html')
@app.route('/create_admin')
def index():
    return render_template('create_admin.html')
@app.route("/create-admin", methods=['POST'])
def create():
    contraseña0 = request.form['password0']
    contraseña1 = request.form['password1']
    if contraseña0 == contraseña1:
        nuevo_empleado = Personal(nombre_del_empleado=request.form['nombre_del_empleado'],apellido_del_empleado=request.form['apellido_del_empleado'],
        nombre_completo_del_empleado=request.form['nombre_del_empleado'] +" "+ request.form['apellido_del_empleado'],
        cedula_de_identidad_del_empleado=request.form['cedula_del_empleado'],numero_telefonico_asignado="+59598"+ str(random.randrange(1000000,9999999)),contraseña_del_empleado = contraseña1)
        db.session.add(nuevo_empleado)
        db.session.commit()
    else:
        return "contraseña incorrecta"
    return render_template('auth.html')


if __name__ == '__main__':
    app.run(debug=True)
    
