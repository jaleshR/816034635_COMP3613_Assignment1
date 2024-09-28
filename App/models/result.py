# App/models/result.py

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)  # Assume this links to a user model
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Result User: {self.user_id}, Competition: {self.competition_id}, Score: {self.score}>'
