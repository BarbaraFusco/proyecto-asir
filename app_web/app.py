# Importar las librerías necesarias
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión SQLAlchemy con Flask
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)


@app.route("/")
def index():
    return render_template('pagina.html', title="Tech Solutions")


@app.route("/contacto", methods=['GET', 'POST'])
def contacto():
    # Si se recibe un formulario (el usuario lo envió)
    if request.method == 'POST':
        db.session.add(Contact(
            # Obtiene el campo "name" del formulario
            name=request.form['name'],
            # Obtiene el campo "email" del formulario
            email=request.form['email'],
            # Obtiene el campo "message" del formulario
            message=request.form['message']
        ))
        # Guarda los cambios en la base de datos
        db.session.commit()
    return render_template('contacto.html', title="Contacto")


# Inicia la base de datos en caso de que no que se haya creado previamente
with app.app_context():
    db.create_all()

# Ejecución de la aplicación
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
