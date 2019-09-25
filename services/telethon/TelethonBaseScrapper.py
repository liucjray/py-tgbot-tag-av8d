from config.config import *
from helpers.Common import *
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


class TelethonBaseScrapper:
    global_config = get_config()
    client = None
    app_api_id = app_api_hash = app_phone = None

    def __init__(self):
        self.set_login_info()

    def get_session_name(self):
        # return self.session_name
        return self.app_phone

    def set_login_info(self):
        self.app_api_id = get_config()['TG']['APP_API_ID']
        self.app_api_hash = get_config()['TG']['APP_API_HASH']
        self.app_phone = get_config()['TG']['APP_PHONE']
        return self

    def set_app_client(self):
        self.client = TelegramClient(self.get_session_name(), self.app_api_id, self.app_api_hash)
        self.client.start()
        self.client.connect()
        return self

    def is_auth(self):
        dump('is_auth')
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.get_session_name())
            self.client.sign_in(self.get_session_name(), input('Enter the code: '))

    def get_groups(self):
        dump('get_groups')
        chats = []
        groups = []
        last_date = None
        chunk_size = 200

        result = self.client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))
        chats.extend(result.chats)

        for chat in chats:
            dump(chat)
            groups.append(chat)
            # try:
            #     if chat.megagroup is True:
            #         channels.append(chat)
            # except:
            #     channels.append(chat)
            #     continue

        i = 0
        for c in groups:
            print(str(i) + '- ' + c.title + ' - ' + str(c.id))
            i += 1

        return groups

    def get_users(self, group):
        dump('get_users')
        users = self.client.get_participants(group, aggressive=True)

        # 資料加入 channel_id
        new_users = []
        for user in users:
            # 字典合併
            new_user = {**user.to_dict(), **{'group_id': group.id, 'group_name': group.title}}
            new_users.append(new_user)

        return new_users
