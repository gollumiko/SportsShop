from flask import Flask,g
import sqlite3
import json

app = Flask(__name__)

DATABASE = 'db/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('db/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()




def get_all_categories(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM category")     
    rows = cur.fetchall()
    categories = []
    for row in rows:
        category = {}
        category['id'] = row[0]
        category['description'] = row[1]
        category['image'] = row[2]
        categories.append(category)
    return categories
     
def get_articles(conn, category_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM article WHERE categoryid=" + category_id)     
    rows = cur.fetchall()
    articles = []
    for row in rows:
        article = {}
        article['id'] = row[0]
        article['description'] = row[1]
        article['price'] = row[2]
        article['image'] = row[3]
        articles.append(article)
    return articles


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    return ""

@app.route("/categories/")
def getCategories():
    conn = get_db()
    categories = get_all_categories(conn)
    return json.dumps(categories, ensure_ascii=False)

@app.route("/categories/<category_id>/articles/")
def getArticles(category_id):
    conn = get_db()
    articles = get_articles(conn, category_id)
    return json.dumps(articles, ensure_ascii=False)


if __name__ == "__main__":
    app.run()