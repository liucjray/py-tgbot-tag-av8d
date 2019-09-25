from services.mongo.AtlasBaseService import *
from repositories.TagAv8dAtlasRepository import *


class TagAv8dAtlasService(AtlasBaseService):
    settings = {'collection': 'av8d'}

    def __init__(self):
        super(TagAv8dAtlasService, self).__init__()
        self.set_repo()

    def set_repo(self, settings=None):
        settings = self.settings if settings is None else settings
        repo = TagAv8dAtlasRepository(settings)
        super(TagAv8dAtlasService, self).set_repo(repo)

    def write(self, updates):
        self.repo.write(updates)
