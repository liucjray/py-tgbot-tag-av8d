from services.telethon.TelethonBaseScrapper import *
from services.mongo.TagAv8dAtlasService import *


class TagAv8dTelethonScrapper(TelethonBaseScrapper):
    global_config = get_config()
    client = None
    app_api_id = app_api_hash = app_phone = None
    atlasSer = None

    def __init__(self):
        self.set_login_info()
        super(TagAv8dTelethonScrapper, self).__init__()
        self.atlasSer = TagAv8dAtlasService()

    def set_login_info(self):
        self.app_api_id = get_config()['TG']['APP_API_ID']
        self.app_api_hash = get_config()['TG']['APP_API_HASH']
        self.app_phone = get_config()['TG']['APP_PHONE']
        return self

    def write(self, updates):
        self.atlasSer.write(updates)

    def test_write_group(self):
        # 爬取 groups 資訊
        self.set_app_client().is_auth()
        groups = self.get_groups()
        g = []
        for grp in groups:
            g.append(grp.to_dict())

        # 寫入 mongodb
        self.atlasSer.set_repo({'collection': 'av8d_group'})
        self.write(g)

    def test_write_group_users(self):
        self.set_app_client().is_auth()
        groups = self.get_groups()

        for grp in groups:
            grp_info = "{}({})".format(grp.title, str(grp.id))
            try:
                users = self.get_users(grp)
                len_users = len(users)

                # 以人數判斷非外部公共群 (如: Python討論群等等)
                if len_users < 100:
                    print('write users...' + grp_info)
                    self.write(users)
                if len_users <= 1:
                    print('no users...' + grp_info)
                    continue
            except Exception as e:
                print(e)
                print('error..' + grp_info)
            finally:
                print('------------------------------------------------------------------')

    def test_read_group_users(self, group_id):
        where = {'group_id': group_id, 'bot': False}
        return self.atlasSer.find(where)
