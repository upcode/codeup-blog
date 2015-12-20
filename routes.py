import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
from datetime import datetime

################################################################################
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
################################################################################
app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)



################################################################################
                        ## BLOG ROUTES ##
################################################################################


   

################################################################################
@app.route("/")
def posts():
    """sort blog list posts by date"""

    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    # posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

################################################################################

@app.route('/posts/<name>/')
def post(name):

    """ list of the posts posted on post.html"""

    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)



################################################################################
@app.route("/articles")
def articles():

    """articles page"""

    return render_template('articles.html')
################################################################################

@app.route("/about-upcode")
def upcode():

    """articles page"""

    return render_template('about-upcode.html')

################################################################################

@app.route("/contact")
def contact():

    """contact page"""

    return render_template('contact.html')


################################################################################



################################################################################
                       ## HELPER FUNCTIONS ##

################################################################################
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)