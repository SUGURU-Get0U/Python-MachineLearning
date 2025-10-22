from flask import Flask, render_template, request

# The render_template makes so instead of running text in the return, it runs HTML templates in a "templates"
# good coding habits:
#  - to name our site "app"

app = Flask(__name__)

# Create functions for our site:
# Create the first Page
    # route -> DNSname.com/this_is_the_route!
    # function -> what whill be on the page
    # Template!
@app.route('/') #This is a DECORATOR!
def hello():
    return 'Hello World'

# Make A dynamic page, for example a users page!
@app.route('/users/<username>')
def users(username):
    return render_template('users.html', username=username)


# Deploy our site
# Only runs the code if it's running from main.py, because we are going to make another pages.py.
if __name__ ==  '__main__':
    app.run(debug=True)

    # makes so we can live edit the code!
    # app.run() deploys the site locally!

    # Heroku SERVER for Deploy!
