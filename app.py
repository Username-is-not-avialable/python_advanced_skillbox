import datetime
from flask import Flask
from random import choice
import re
import os

app = Flask(__name__)

CARS = ['Chevrolet', 'Renault','Ford',
'Lada']
CATS = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_book_words(filename):
    BOOK_FILE = os.path.join(BASE_DIR, filename)
    with open(BOOK_FILE) as book:
        words = re.findall(r'\w+', book.read())
        return words

WORDS = get_book_words('war_and_peace.txt')


@app.route('/test')
def test_function():
    now = datetime.datetime.now()
    return f'Это тестовая страничка, ответ сгенерирован в {now}'



@app.route('/hello_world')
def hello_world_function():
    return f'Привет, мир!'



@app.route('/cars')
def cars_function():
    return ', '.join(CARS)


@app.route('/cats')
def cats_function():
    return choice(CATS)

@app.route('/get_time/now')
def time_now_function():
    current_time = datetime.datetime.now().utcnow()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def time_future_function():
    current_time = datetime.datetime.now().utcnow()
    hour = datetime.timedelta(hours=1)
    return f'Точное время через час будет: {current_time+hour}'


@app.route('/get_random_word')
def random_word_function():
    return choice(WORDS)

@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Количество открытий данной страницы: {counter.visits}'


counter.visits = 0