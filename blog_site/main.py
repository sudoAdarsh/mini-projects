from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    return post.home()

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    return post.render(blog_id)

if __name__ == "__main__":
    app.run(debug=True)
