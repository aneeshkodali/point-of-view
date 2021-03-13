# python imports
from mongoengine import Document
import datetime

# project imports
from models.default_values import uuid_value, current_timestamp

class BaseMixin(Document):
    '''
    Base model from which all other tables inherit
    '''


    # allows for 'inheritance' while allowing other models to be created as separate collections
    meta = {'abstract': True}

    def as_dict(self):

        self_dict = {}

        for field in self._fields:
            # handle dates
            if isinstance(self[field], datetime.date):
                self_dict[field] = self[field].isoformat()
            else:
                self_dict[field] = self[field]
        return self_dict