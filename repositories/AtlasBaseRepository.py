from pymongo import MongoClient
from config.config import *
from helpers.Common import *


class AtlasBaseRepository:
    global_config = get_config()
    prepares = []
    collection = None

    def __init__(self, settings):
        self.settings = settings
        self.collection = self.get_collection(self.settings['collection'])

    def get_collection(self, collection):
        client = MongoClient(self.global_config['MONGODB']['CONNECTION_ATLAS'])
        mongo_collection = client.get_database(self.global_config['MONGODB']['DB'])[collection]
        return mongo_collection

    def write_prepare(self, updates):
        self.prepares = []

        # 若只傳入一筆 dict 資料則使用 list 包裝
        if isinstance(updates, dict):
            updates = [updates]

        for update in updates:
            # 統一轉換為 dict
            if not isinstance(update, dict):
                update = update.to_dict()

            # 判斷後寫入
            chat_id = dict_get(update, "message.chat.id", 0)
            if int(chat_id) == int(self.settings['chat_id']):
                self.prepares.append(update)

    def write(self, updates):
        dump('AtlasBaseRepo.write')
        try:
            self.write_prepare(updates)
            if self.prepares:
                self.collection.insert_many(self.prepares, ordered=False)
        except Exception as e:
            print(__file__, e)

    def get_data_exist(self):
        return self.collection.find({'is_deleted': None})

    def find(self, where={}):
        return self.collection.find(where)

    def find_one(self, where={}):
        return self.collection.find_one(where)

    def delete(self, where={}, update={}):
        self.collection.update_one(where, update)

    def update(self, where={}, update={}):
        self.collection.update_one(where, update)

    def read(self):
        limit = self.global_config['MONGODB'].getint('READ_DOCS_LIMIT', 200)
        return self.collection \
            .find() \
            .sort('update_id', -1) \
            .limit(limit)
