from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Read headers from the request
    headers = {key: value for key, value in request.headers.items()}
    return render_template('index.html', headers=headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
