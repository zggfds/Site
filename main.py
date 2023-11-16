from flask import Flask, render_template, request
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
x = "САша"
luboe_name = {
    "name": x,
    "age": "100000"
}

spisok = ["дрель","перфоратор","янтарь","алмаз","хз что еще лол"]

img = ["https://rosspectr.ru/wp-content/uploads/f/b/9/fb91fb7fcf48f3d92b15f904bd1d5ef4.jpeg","https://images.zakupka.com/i3/firms/27/28/28527/festivalnyy-amazon-eto-prazdnik-kazhdyy-den_b576b4dcb53cd86_800x600.jpg"]

@app.route('/')
def index_pade():
    return render_template('index (3).html')

@app.route('/sec')
def index1():
    name = 4
    lol = 99
    x = lol+name

    return render_template("index.html", name=luboe_name, spisok = spisok, imgy = img)
    a = request.form['name']
    print(a)


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    return render_template("yey.html")


@app.route('/run', methods=['POST'])
def reg_run():
    a = request.form['name']
    b = request.form['pass']
    if a == "Саша":
        if b == "qwerty75":
            return "все гуд"
        else:
            return "Невнрный пароль"
    else:
        return "Невнрный логин"



if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)