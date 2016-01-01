Python Flask Blog
STACK: 
Python 
Flask 
Jinja 
Javascript 
HTML 
CSS 
Heroku 
Markdown

Created Programming Blog using Flask framework. This is a static site using markdown for occasional writing. 
Posts are composed in Markdown which includes ability for code snuppets. 

Requirements:
Python dependencies: 
Flask==0.10.1
Flask-FlatPages==0.5
Frozen-Flask==0.11
Jinja2==2.7.1
Markdown==2.3.1
MarkupSafe==0.18
PyYAML==3.10
Pygments==1.6
Werkzeug==0.9.3
itsdangerous==0.22
wsgiref==0.1.2

After creating virutal env drop list above in to command line and 

execute pip install -r requirements.txt from your shell. 

FOLDER STRUCTURE
create folders to store static markdown pages. Should have 4 directories, 2 files
├── blog.py
├── content
│   └── posts
│       └── firstpost.md
├── static
└── templates


THE ROUTES FILE

import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)


Before this line --> if __name__ == "__main__" add the following:
@app.route("/posts/")
def posts():
    #iterate over the list and sort posts by date  
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


TEMPLATES
Create template for posts.html for list of posts --> here is minimal skelton of post templates

{% for post in posts %}
    <a href="{{ url_for('post', name=post.path.replace('posts/', '')) }}">
        {{ post.title }}
    </a>
    <small>{{ post.date }}</small>
{% endfor %}

create template for post.html 
And for post.html, drop the following into your template wherever you want them displayed!
{{ post.html|safe }}
{{ post.title }}
{{ post.date }}

NEXT: creating Markdown for posts
POSTS
store your markdown files in the content/posts/ directory as some_file_name.md, and include a small amount of metadata in each file.
title: Should it be YYYY-MM-DD or YYYY-DD-MM
date: 2013-08-27

DEPLOY / SHIP IT
If you want to run this server to test on your local machine, you can simply run the script using python blog.py.
 or you can deply to heroku or github pages



