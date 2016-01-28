<h1>Python Flask Blog</h1>
<lable> TECH STACK:</label>
<ul>
<li>Python</li> 
<li>Flask</li> 
<li>Jinja </li>
<li>Javascript </li>
<li>HTML </li>
<li>CSS </li>
<li>Heroku </li>
<li>Markdown</li>
</ul>
<p>Created Programming Blog using Flask framework. This is a static site using markdown for occasional writing. 
Posts are composed in Markdown which includes ability for code snuppets.</p>
<lable> Requirements:</label>
<p>Python dependencies:</p>
<ul>
<li>Flask==0.10.1</li>
<li>Flask-FlatPages==0.5</li>
<li>Frozen-Flask==0.11</li>
<li>Jinja2==2.7.1</li>
<li>Markdown==2.3.1</li>
<li>MarkupSafe==0.18</li>
<li>PyYAML==3.10</li>
<li>Pygments==1.6</li>
<li>Werkzeug==0.9.3</li>
<li>itsdangerous==0.22</li>
<li>wsgiref==0.1.2</li>
</ul>

<p>After creating virutal env drop list above in to command line and</p> 

<p>execute pip install -r requirements.txt from your shell.</p> 

<h1>FOLDER STRUCTURE</h1>
<p>create folders to store static markdown pages. Should have 4 directories, 2 files
├── blog.py
├── content
│   └── posts
│       └── firstpost.md
├── static
└── templates<p>


<h1>THE ROUTES FILE</h1>

<p>import sys</p>
<p>from flask import Flask, render_template</p>
<p>from flask_flatpages import FlatPages, pygments_style_defs</p>
<p>from flask_frozen import Freezer</p>

<p>DEBUG = True</p>
<p>FLATPAGES_AUTO_RELOAD = DEBUG</p>
<p>FLATPAGES_EXTENSION = '.md'</p>
<p>FLATPAGES_ROOT = 'content'</p>
<p>POST_DIR = 'posts'</p>

<p>app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)</p>

<p>if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)</p>


<p>Before this line --> if __name__ == "__main__" add the following:</p>
<p>@app.route("/posts/")
def posts():
    #iterate over the list and sort posts by date  
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)</p>

<p>@app.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)</p>


<h1>TEMPLATES</h1>
<p>Create template for posts.html for list of posts --> here is minimal skelton of post templates</p>

<p>{% for post in posts %}
    <a href="{{ url_for('post', name=post.path.replace('posts/', '')) }}">
        {{ post.title }}
    </a>
    <small>{{ post.date }}</small>
{% endfor %}</p>

<p>create template for post.html 
And for post.html, drop the following into your template wherever you want them displayed!
{{ post.html|safe }}
{{ post.title }}
{{ post.date }}<p>

<h1>NEXT: creating Markdown for posts</h1>
POSTS
store your markdown files in the content/posts/ directory as some_file_name.md, and include a small amount of metadata in each file.
title: Should it be YYYY-MM-DD or YYYY-DD-MM
date: 2013-08-27</p>

<h1>DEPLOY / SHIP IT</h1>
<p>If you want to run this server to test on your local machine, you can simply run the script using python blog.py.
 or you can deply to heroku or github pages</p>



