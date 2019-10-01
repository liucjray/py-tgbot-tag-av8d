import telegram
from config.config import *
from helpers.Common import *
from services.mongo.TagAv8dAtlasService import *


class TelegramBase:
    global_config = get_config()
    settings = None
    bot = None

    def __init__(self, settings=None):
        self.set_settings(settings)
        self.set_bot()

    def set_settings(self, settings):
        self.settings = self.get_default_settings() if settings is None else settings

    def get_default_settings(self):
        return {
            'token': self.global_config['TG']['token']
        }

    def set_bot(self):
        self.bot = telegram.Bot(token=self.settings['token'])

    def tag_av8d(self, group_id):
        # 轉換對應儲存的 group_id
        group_ids = [
            abs(group_id),
            abs(int(str(group_id)[3:]))
        ]

        for chat_id in group_ids:
            # users 須包含 user_id & user_name
            service = TagAv8dAtlasService()
            users = service.find({'group_id': chat_id, 'bot': False})

            # 組合 tag 語句
            texts = []
            for user in users:
                # 若有 username 則取為 @username
                name = user['first_name']
                if user['username'] is not None and len(user['username']) > 0:
                    name = '@' + user['username']
                text = '<a href="tg://user?id={}">{}</a>'.format(user['id'], name)
                # text = '[{}](tg://user?id={}) \n'.format(name, user['id'])
                texts.append(text)

            # 以十人為一次發送的單位
            chunks_texts = chunks(texts, 5)

            # 每十人傳一次訊息,避免標記後未顯示驚嘆號
            for texts in chunks_texts:
                msg = " | ".join(texts)
                self.bot.send_message(group_id, msg, parse_mode="HTML")

    def test_tag_av8d(self):
        self.tag_av8d(1129608054)
