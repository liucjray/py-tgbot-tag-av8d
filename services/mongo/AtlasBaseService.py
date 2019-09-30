from repositories.AtlasBaseRepository import *


class AtlasBaseService:
    global_config = get_config()
    repo = None

    def __init__(self):
        pass

    def set_repo(self, repo):
        self.repo = repo

    def write_prepare(self, updates):
        self.repo.write_prepare(updates)

    def write(self, updates):
        dump('AtlasBaseService.write')
        self.repo.write(updates)

    def get_data_exist(self):
        return self.repo.get_data_exist()

    def find(self, where={}):
        return self.repo.find(where)

    def find_one(self, where={}):
        return self.repo.find_one(where)

    def delete_by_group_id(self, group_id):
        # dump('AtlasBaseService.delete_by_group_id')
        self.repo.delete_by_group_id(group_id)

    def update(self, where={}, update={}):
        self.repo.update_one(where, update)

    def read(self):
        limit = self.global_config['MONGODB'].getint('READ_DOCS_LIMIT', 200)
        return self.repo \
            .find() \
            .sort('update_id', -1) \
            .limit(limit)
