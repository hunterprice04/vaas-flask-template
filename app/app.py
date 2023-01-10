from flask import Flask, render_template
app = Flask(__name__)

"""
Uncomment the following lines to enable CORS
"""
# from flask_cors import CORS, cross_origin
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=["GET", "POST"])
# @cross_origin()
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')