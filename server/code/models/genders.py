from db import db
import json

class GenderModel(db.Document):
    '''
    Genders
    '''

    gender_id = db.IntField(primary_key=True)            
    abbreviation = db.StringField()
    gender = db.StringField()

    meta = {'collection': 'genders'}

    def json(self):
        return json.loads(self.to_json())

    @classmethod
    def find_by_gender_id(cls, gender_id):
        return GenderModel.objects(gender_id=gender_id).first()
    
    @classmethod
    def find_by_abbreviation(cls, abbreviation):
        return GenderModel.objects(abbreviation=abbreviation).first()

    @classmethod
    def find_by_gender(cls, gender):
        return GenderModel.objects(gender=gender).first()