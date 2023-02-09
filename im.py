from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def begin():
    return "Миссия <br> Колонизация Марса"


@app.route('/index')
def page2():
    return "<p>И на Марсе</p> <p>будут яблони цвести!</p>"


@app.route('/promotion')
def page3():
    d = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
         "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    s = '</p><p>'.join(i for i in d)
    return f"<p>{s}</p>"

@app.route('/image_mars')
def page4():
    return '''<p>Жди нас, Марс!</p>
    <p><img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась"></p>
    <p>Вот она какая, красная планета!</p>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
