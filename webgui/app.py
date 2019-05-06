#
# Python app for simple webpgae
#

import impl

from flask import Flask, render_template, request

app = Flask(__name__)

# Simple hello world test
@app.route('/')
def hello():
    return render_template('home.html')

# try to display a figure
@app.route('/plot.png')
def print_fig():
    return impl.fig_to_flask()


# method to call constructor
def findRecommendations(input_media):
    if input_media == "":
        raise RuntimeError("no data to infer new favorite movies")

    return input_media + ["Pokemon", "Dragonball Z", "Toy Story", "Cars"]

# render the webpage after list request
@app.route('/handle_input', methods=['POST'])
def handle_input():
    input_media = request.form['inputMedia']
    input_media = input_media.split(',')
    recs = findRecommendations(input_media)
    return render_template('home.html', recs=recs)

# run the application
if __name__ == "__main__":
    app.run()
