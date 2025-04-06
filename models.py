# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Album(db.Model):
    __tablename__ = 'albums'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    
    def __init__(self, title, artist, genre, release_date):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.release_date = release_date

    def __repr__(self):
        return f"<Album {self.title} by {self.artist}>"
