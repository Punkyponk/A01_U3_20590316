# app.py

from flask import Flask, render_template
from models import db, Album
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://samvela_8xau_user:NfJXKKKbJGQK1EjjlKMcfisBjWZaeTEk@dpg-cvnl9are5dus738ks7r0-a.oregon-postgres.render.com/samvela_8xau'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)

@app.route('/')
def index():
    # Recuperamos todos los albums desde la base de datos
    albums = Album.query.all()
    return render_template('index.html', albums=albums)

if __name__ == "__main__":
    app.run(debug=True)
