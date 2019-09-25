from repositories.AtlasBaseRepository import *


class TagAv8dAtlasRepository(AtlasBaseRepository):
    def write(self, updates):
        try:
            for _update in updates:
                # 唯一索引
                _filter = {
                    'group_id': _update['group_id'],
                    'id': _update['id'],
                }
                self.collection.update_many(
                    _filter,
                    {'$set': _update},
                    upsert=True
                )
        except Exception as e:
            print(__file__, e)

    def get_users(self, group_id):
        group_id = 320735075
        users = self.find({'group_id': group_id})
        print(users)
