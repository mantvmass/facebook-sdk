from flask import request, url_for, render_template
import requests
from facebook import GraphAPI
from app import app



index = 3 # declare total page query

token = "your access token"

graph = GraphAPI(token)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass
    j = graph.getcontent(id="your id", data="posts.limit(3){message,full_picture,id,story,updated_time,created_time}")
    print(j)
    return render_template('index.html', data=j)