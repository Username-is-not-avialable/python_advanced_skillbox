from datetime import datetime
from flask import Flask

app = Flask(__name__)

def get_ending():
    weekday = datetime.today().weekday()
    if weekday in (0,1,3,6):
        ending = "его "
    else:
        ending = "ей "
    weekdays = ('понедельника', "вторника", "среды", "четверга", "пятницы", "субботы", "воскресенья")
    phrase_ending = ending + weekdays[weekday]
    return phrase_ending
@app.route('/hello_world/<name>')
def hello_world(name):
    ending = get_ending()
    return f'Привет, {name}. Хорош{ending}!'


if __name__ == '__main__':
    app.run(debug=True)