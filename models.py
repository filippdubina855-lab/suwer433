from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class HomeWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    group = db.Column(db.String(100), nullable=False)
    header_url = db.Column(db.String(500), nullable=True)