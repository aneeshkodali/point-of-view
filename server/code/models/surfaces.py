from db import db
import json

class SurfaceModel(db.Document):
    '''
    Court surfaces
    '''

    surface_id = db.IntField(primary_key=True)            
    surface = db.StringField()

    meta = {'collection': 'surfaces'}

    def json(self):
        return json.loads(self.to_json())

    @classmethod
    def find_by_surface_id(cls, surface_id):
        return SurfaceModel.objects(surface_id=surface_id).first()
    
    @classmethod
    def find_by_surface(cls, surface):
        return SurfaceModel.objects(surface=surface).first()