# app.py

from flask import Flask, render_template, request, redirect, url_for
from models import db, Album
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://samvela_5p8g_user:RHlKzHOd8J3aqEmyc4to4rSo90hioz6e@dpg-d0h860q4d50c73b9q14g-a.oregon-postgres.render.com/samvela_5p8g'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db.init_app(app)

@app.route('/')
def index():
    # Recuperamos todos los albums desde la base de datos
    albums = Album.query.all()
    return render_template('index.html', albums=albums)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        title = request.form['title']
        artist = request.form['artist']
        genre = request.form['genre']
        release_date = datetime.strptime(request.form['release_date'], '%Y-%m-%d')  # Convertimos la fecha a formato Date
        
        # Creamos el nuevo album
        new_album = Album(title=title, artist=artist, genre=genre, release_date=release_date)
        
        # Guardamos en la base de datos
        db.session.add(new_album)
        db.session.commit()
        
        # Redirigimos a la página principal (index)
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    # Recuperamos el álbum a editar
    album = Album.query.get_or_404(id)
    
    if request.method == 'POST':
        # Actualizamos los datos del álbum con los nuevos valores
        album.title = request.form['title']
        album.artist = request.form['artist']
        album.genre = request.form['genre']
        album.release_date = datetime.strptime(request.form['release_date'], '%Y-%m-%d')  # Convertimos la fecha
        
        # Guardamos los cambios en la base de datos
        db.session.commit()
        
        # Redirigimos a la página principal (index)
        return redirect(url_for('index'))
    
    return render_template('update.html', album=album)

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    # Recuperamos el álbum a eliminar
    album = Album.query.get_or_404(id)
    
    # Eliminamos el álbum de la base de datos
    db.session.delete(album)
    db.session.commit()
    
    # Redirigimos a la página principal (index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

