# py-tgbot-tag-av8d

## 專案使用套件
+ [Telethon](https://github.com/LonamiWebs/Telethon)
   - 用途: 爬取群組所有用戶資訊
+ [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
   - 用途: 發送訊息資訊 & polling

## 專案配置說明
+ config/config.ini
   - [TG]
      - TOKEN: bot token
      - APP_API_ID: 用戶 app_api_id
      - APP_API_HASH: 用戶 app_api_hash
      - APP_PHONE: 用戶 app_phone
   - [MONGODB]
      - CONNECTION_ATLAS: atlas mongodb 服務
      - DB: collection
      - READ_DOCS_LIMIT: 200
+ scrapper.py
   - 爬取所有群組用戶並寫入 mongodb
   - 需配置排程定期爬取新用戶
   - 若群組越多所需時間越長
+ polling.py
   - 監控 telegram bot command
   - 需背景執行

## 第一次執行 scrapper.py 所需輸入資訊 (模仿用戶實際登入)
+ Please enter your phone (or bot token): 輸入電話號碼
+ Please enter the code you received: 輸入驗證碼

## 取得 app_api_id, app_api_hash 方式
+ https://my.telegram.org