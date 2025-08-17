# This file implements the routing used for the Flask frontend user interface

from flask import Flask, render_template, redirect, url_for, request
from itemlist import ItemList

app = Flask(__name__)
items = ItemList('CS210_Project_Three_Input_File.txt')


@app.route('/')
def index():
    return render_template('index.html', items=items.items)


@app.route('/increase/<item>')
def increase(item):
    items.add_or_increment(item)
    return redirect(url_for('index'))


@app.route('/decrease/<item>')
def decrease(item):
    items.decrement(item)
    return redirect(url_for('index'))


@app.route('/add', methods=['POST'])
def add():
    new_item = request.form['new_item']
    if new_item:
        items.add_or_increment(new_item)
    return redirect(url_for('index'))


@app.route('/sort_frequency')
def sort_frequency():
    items.sort_by_frequency()
    return redirect(url_for('index'))


@app.route('/sort_name')
def sort_name():
    items.sort_by_name()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
