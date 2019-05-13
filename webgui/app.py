#
# Python app for simple webpgae
#

import impl
import flask

# globals
app = flask.Flask(__name__)

md = impl.MovieDriver()
skl = impl.ScikitInfer(md.getData(), md.getLabels())


# Simple hello world test
@app.route('/')
def hello():
    return flask.render_template('home.html')

# try to display a figure
@app.route('/plot.png')
def print_fig():
    return impl.figToFlask()


# method to call constructor
def findRecommendations(input_media):
    return input_media + ["Pokemon", "Dragonball Z", "Toy Story", "Cars"]

# render the webpage after list request
@app.route('/handle_input', methods=['POST'])
def handle_input():
    input_media = flask.request.form['inputMedia']
    input_media = input_media.split(',')
    recs = findRecommendations(input_media)
    return flask.render_template('home.html', recs=recs)

# run the application
if __name__ == "__main__":
    app.run()
