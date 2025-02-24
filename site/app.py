from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('my_base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT text_1 FROM data LIMIT 1')
    text_1 = cursor.fetchone()[0]
    
    return render_template('home_page.html', text=text_1)


@app.route('/politics')
def politics():
    conn = sqlite3.connect('my_base.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT text_2 FROM data LIMIT 1')
    text_2 = cursor.fetchone()[0]    
    
    return render_template("politics_page.html", pic = text_2)


@app.route('/economy')
def economy():
    return render_template("economy_page.html")


@app.route('/sport')
def sport():
    return render_template("sport_page.html")


if __name__ == "__main__":
    app.run(debug=True)