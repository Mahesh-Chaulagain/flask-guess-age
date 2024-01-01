# Jinja
# -> a modern and designer-friendly templating language for python
# -> specify which part be evaluated as python code inside the html file
# -> when import is required in html file then it is best to write the code in python server
# -> use double curly braces {{  }} in html file inorder to create single line of python expression
# -> use curly braces with percentage sign {% %} for multiline python statement

# Url Building
# ->To build a URL to a specific function, use the url_for() function.
# ->It accepts the name of the function as its first argument and any number of keyword arguments,
#   each corresponding to a variable part of the URL rule.
# -> Unknown variable parts are appended to the URL as query parameters.

from flask import Flask, render_template
import random, requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    today = datetime.now()
    current_year = today.year
    your_name = "Mahesh Chaulagain"

    # pass over the "num" variable after the html file is rendered
    return render_template("index.html", num=random_number, year=current_year, name=your_name)

@app.route("/guess/<name>")
def make_guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    if gender == "male":
        img_url = "https://media.giphy.com/media/26xBtZesne83bPFHW/giphy.gif"

    else:
        img_url = "https://media.giphy.com/media/H5iz8vPzfaYBr0dWK1/giphy.gif"

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess.html", person_name=name, gender=gender, age=age , image=img_url)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/f8b9cce0347af5bc4402"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)