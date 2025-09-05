from flask import Flask, redirect, render_template, url_for, request
from models.usuariosModel import Usuario, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.route("/crearDB")
def crearDB():
    db.create_all()
    return redirect(url_for("login"))

@app.route("/login", methods=['POST', 'GET'])
def login():
#    if request.method == 'GET':
    return render_template("login.html")
#   else:
#        email = request.form['email']   
#        password = request.form['password']
        

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        nombre = request.form['name']    
        mail = request.form['email']    
        contraseña = request.form['password']    

        nuevoUsuario = Usuario(nombre, mail, contraseña, 'admin')
        db.session.add(nuevoUsuario)
        db.session.commit()
        return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)