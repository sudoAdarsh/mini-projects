import requests
from flask import render_template

class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.blog_data = self.all_posts()

    def all_posts(self):
        return requests.get(self.blog_url).json()

    def home(self):
        return render_template("index.html", blogs=self.blog_data)
    
    def render(self, blog_id):
        for blog in self.blog_data:
            if blog["id"] == blog_id:
                return render_template("post.html", **blog)