import json

from db import db
from uuid import uuid4

class BaseModel(db.Document):
    '''
    Base model used to build other models
    '''

    uid = db.UUIDField(unique=True, nullable=False, default=lambda: uuid4())

    # allows for 'inheritance' while allowing other models to be created as separate collections
    meta = {'abstract': True}

    # return json representation of record
    def json(self):
        return json.loads(self.to_json())

    # queries model for record based on the primary key
    @classmethod
    def find_by_id(cls, id):
        return cls.objects(pk=id).first()