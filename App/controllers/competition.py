# App/controllers/competition.py

from App.models.competition import Competition
from App.database import db

class CompetitionController:
    def create_competition(name, description, date):
        new_competition = Competition(name=name, description=description, date=date)
        db.session.add(new_competition)
        db.session.commit()
        return new_competition
    
    def get_competitions():
        return Competition.query.all()
    
    def get_competition_results(competition_id):
        competition = Competition.query.get(competition_id)
        if competition:
            return competition.results
        return None
