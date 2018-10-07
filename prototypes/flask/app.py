from flask import Flask, render_template, request, redirect
import psycopg2
from argon2 import PasswordHasher

app = Flask(__name__)

@app.route('/')
@app.route('/index.html', methods=['GET','POST'])
def home_page():
    if request.method == 'POST':
            data = request.form
            print(data)
            hashedPassword = ph.hash(data["password"])
            cur.execute("insert into users values('" + data["username"] + "','" + hashedPassword + "','" + data["firstname"] + "','" + data["lastname"] + "','" + data["emailid"] + "','" + data["phone"] + "');")
            conn.commit()
    return render_template('index.html')

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')
    
@app.route('/listings_single.html')
def listings_single():
    return render_template('listings_single.html')

@app.route('/listings.html')
def listings():
    return render_template('listings.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/post-ad.html')
def post_ad_page():
    return render_template('post-ad.html')

@app.route('/register.html')
def register_page():
    return render_template('register.html')

if __name__ == '__main__':
    conn = psycopg2.connect(database="forsale", user="root", password="root", host="localhost")
    cur = conn.cursor()
    ph = PasswordHasher()
    app.run()
