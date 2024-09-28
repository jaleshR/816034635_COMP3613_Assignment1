# App/controllers/competition.py

from datetime import datetime
from App.models.competition import Competition
from App.database import db

def create_competition(name, description, date):
    # Convert date string (e.g., "2024-09-20") to a datetime.date object
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Incorrect date format, should be YYYY-MM-DD: {date}")

    # Create a new Competition instance
    new_competition = Competition(name=name, description=description, date=date_obj)
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
