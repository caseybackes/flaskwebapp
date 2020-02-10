
# Demonstrates Bootstrap version 3.3 Starter Template
# available here: https://getbootstrap.com/docs/3.3/getting-started/#examples

from flask import Flask, render_template
app = Flask(__name__)

# home page
@app.route('/')
def index():
    context = {"title":"Home"}
    return render_template('index.html', context=context)

@app.route('/about')
def about():
    context = {"title":"About"}
    return render_template('about.html', context = context)

@app.route('/contact')
def contact():
    context = {'title':"Contact"}
    return render_template('contact.html', context=context)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False)
