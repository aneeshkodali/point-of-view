import mongoengine as db
import json

from models.default_values import default_uuid_value

class BaseModel(db.Document):
    '''
    Base model used to build other models
    '''

    #uuid = db.StringField(unique=True, nullable=False, default=default_uuid_value)

    # allows for 'inheritance' while allowing other models to be created as separate collections
    meta = {'abstract': True}

    # return json representation of record
    def json(self):
        return json.loads(self.to_json())
