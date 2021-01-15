from db import db
import json

class BaseModel(db.Document):
    '''
    Base model used to build other models
    '''

    # allows for 'inheritance' while allowing other models to be created as separate collections
    meta = {'abstract': True}

    # return json representation of record
    def json(self):
        return json.loads(self.to_json())

    # queries model for record based on the primary key
    @classmethod
    def find_by_id(cls, id):
        return cls.objects(pk=id).first()