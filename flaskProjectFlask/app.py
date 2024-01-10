from flask import Flask

app = Flask(__name__,
        template_folder = "templates",
        static_folder = "static",
        static_url_path = "/static-files/",  # Путь, по которому можно получить файлы их папки `static_folder`.
)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/main')
def mainn():  # put application's code here
    return 'Hello World!'
