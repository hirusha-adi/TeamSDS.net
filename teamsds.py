from flask import Flask, render_template, send_file, url_for
from utils import Config

app = Flask(__name__)


@app.route('/')
def comingsoon():
    return render_template(
        'comingsoon.html',
        page_title="TeamSDS | Coming Soon!"
    )


def runWebServer():
    app.run(
        Config.host,
        port=Config.port,
        debug=Config.debug
    )


if __name__ == '__main__':
    runWebServer()
