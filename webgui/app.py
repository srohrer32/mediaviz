#
# Python app for simple webpgae
#

import impl
import flask

# globals
app = flask.Flask(__name__)

md = impl.MovieDriver()
skl = impl.ScikitInfer(md.getData(), md.getLabels())

#skl.buildEngine()


# Simple hello world test
@app.route('/')
def init_page():
    return flask.render_template('home.html')


# try to display a figure
@app.route('/plot.png')
def print_fig():
    return impl.figToFlask()


# render the webpage after list request
@app.route('/handle_input', methods=['POST'])
def handle_input():
    input_media = flask.request.form['inputMedia'].split(',')
    valid_in = impl.findMembers(input_media, md.getLabels())
    recs = skl.inferFromData(valid_in)
    return flask.render_template('home.html', recs=recs)


# run the application
if __name__ == "__main__":
    app.run()
