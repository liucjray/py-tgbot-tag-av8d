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
                text = '[{}](tg://user?id={})'.format(user['first_name'], user['id'])
                texts.append(text)
            msg = " ".join(texts)

            try:
                self.bot.send_message(group_id, msg, parse_mode="Markdown")
                # 若无错误抛出则跳出迴圈
                break
            except Exception as e:
                dump(e)
                continue

    def test_tag_av8d(self):
        self.tag_av8d(1341783380)
