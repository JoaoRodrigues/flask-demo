"""
Demo Flask application.
"""

from flask import Flask
from flask import render_template
from flask import request

from auxfuncs import load_ingredients

app = Flask(__name__)

# we load this once when the app first loads.
ingredients = load_ingredients()

# Routes map functions to a url
# route('/') is the home page of your app.
# Whatever the route returns is rendered as HTML.
@app.route('/')
def homepage():

    # Otherwise, we render the homepage
    #
    # Templates help you separate the dynamic Python code
    # from static HTML pages, CSS, etc.
    # You should store them in the templates/ folder.

    # We can pass variables to the template too, to help
    # us render the page in different ways!
    return render_template('home.html', ingredients=ingredients)


@app.route('/summary', methods=['POST'])
def summary():
    if request.method == 'POST':  # did we press the submit button?
        formdata = request.form  # we get the data from the HTML form

        costsum = 0.0
        for key in formdata.keys():  # keys are checkbox ids
            costsum += float(formdata[key])  # values are the costs

        if costsum > 20:
            comment = 'Big spender!'
        elif costsum > 10:
            comment = "Fair enough.."
        else:
            comment = "Easy there cheapo!"

        return render_template(
            'summary.html',
            total_cost=costsum,
            comment=comment
        )


if __name__ == '__main__':
    app.run(debug=True)  # set debug to False when you deploy!