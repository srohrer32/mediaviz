#
# Python app for simple webpgae
#

import io
import random
from flask import Flask, render_template, request, Response

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

# Simple hello world test
@app.route('/')
def hello():
    return render_template('home.html')

# try to display a figure
@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

@app.route('/handle_input', methods=['POST'])
def handle_input():
    projectdat = request.form['inputMedia']
    print("project dat var read is = ", projectdat)
    return render_template('home.html')

# run the application
if __name__ == "__main__":
    app.run()
