# App/controllers/result.py

import csv
from App.models.result import Result
from App.database import db

class ResultController:
    def import_results(file_path, competition_id):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                result = Result(user_id=row['user_id'], competition_id=competition_id,
                                score=row['score'], ranking=row['ranking'])
                db.session.add(result)
            db.session.commit()
