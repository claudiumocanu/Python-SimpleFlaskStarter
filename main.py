from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("dashboard.html")


# Simple get mapping
@app.route('/hello')
def hello():
    return 'Hello world'

# Simple get mapping with one string argument passed
@app.route('/profile/<username>')
def profile(username):
    return '<h3>Username: {}</h3>'.format(username)

# Simple get mapping wiht integer argument passed
@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h3>Post id: {}</h3>'.format(post_id)


# Single url handling both GET and POST requests
@app.route('/api/req', methods=['GET', 'POST'])
def api_req():
    if request.method == 'GET':
        return 'Request type: {}'.format(request.method)
    if request.method == 'POST':
        return 'Request type: {}'.format(request.method)


# Simple template rendering
@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("dashboard.html")

#
#
#
# Run app only if ran directly
if __name__ == "__main__":
    app.run(debug=False)
