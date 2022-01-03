# from flask import Flask
# MSG = "heyhey"
# app = Flask(__name__)

# @app.route("/")
# def get_secret_message():
#     return MSG + "/n"

# if __name__ == "__flask__":
#     app.run(port=5684) 

from flask import Flask
from flask import render_template
from flask import request
from block import write_block, check_integrity
app = Flask(__name__ ,template_folder='templates')

#decorater for handling requests
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form.get('data')
        timestamp = request.form.get('timestamp')
        # amount = request.form.get('amount')
        

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) 

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# app.run()
