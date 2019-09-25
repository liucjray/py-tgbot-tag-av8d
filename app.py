from flask import Flask, render_template, request
from config.config import *
from services.telegram.TelegramBase import *


def create_app():
    my_app = Flask(__name__)
    return my_app


app = create_app()


@app.route('/')
def index():
    return '9487 OK!'


@app.route('/set_webhook')
def set_webhook():
    msg = TelegramBase().bot.send_message('-320735075', 'qqq')
    return msg


@app.route('/get_updates')
def get_updates():
    global_config = get_config()
    token = global_config['TG']['TOKEN']
    url = "https://api.telegram.org/bot{}/getUpdates".format(token)
    return "<a href={} target=_blank>getUpdates()</a>".format(url)


@app.route('/test')
def test():
    tb = TelegramBase()
    tb.test_tag_av8d()
    return 'OK'


if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port=9487)
