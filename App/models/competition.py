# App/models/competition.py

from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)

    results = db.relationship('Result', backref='competition', lazy=True)

    def __repr__(self):
        return f'<Competition {self.name}>'
