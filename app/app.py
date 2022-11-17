from flask import Flask, render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

# @app.route('/api/v1/register_pond')
# def hello():
#     return

@app.post('/api/v1/register_pond')
def register_pond():
    name = request.form['name']
    location = request.form['location']
    material = request.form['material']
    shape = request.form['shape']
    pond={
        'name':name,
        'location' : location,
        'material' : material,
        'shape' : shape
    }
    app.logger.debug("Debug", name)
    data={}
    return pond


if __name__ == '__main__':
    app.run()