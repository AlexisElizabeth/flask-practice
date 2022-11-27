import os

from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)

YOUR_NAME = "Alexis Elizabeth Paluch"
AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://gender-api.com/get"
GENDERIZED_KEY = os.getenv("GENDERIZED_KEY")


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("mywebsite.html", num=random_number, year=current_year, name=YOUR_NAME)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"https://api.agify.io/?name={name}")
    age_data = response.json()
    predicted_age = age_data["age"]

    response = requests.get(url=f"https://gender-api.com/get?name={name}&country=CA&key={GENDERIZED_KEY}")
    gender_data = response.json()
    predicted_gender = gender_data["gender"]
    return render_template("guess.html", name=name, age=predicted_age, gender=predicted_gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
