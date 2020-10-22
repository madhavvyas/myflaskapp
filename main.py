from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'name': 'Mark Smith'}

api.add_resource(HelloWorld, '/apiengine')

# URL mapped with Method
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about-us')
def aboutus():
    return "I am from About us"

@app.route('/greet/<personname>')
def greetuser(personname):
    return "Good Morning! " + str(personname)

@app.route('/privacy-policy')
def privacyPolicy():
    return "I am from Privacy Policy 123"

# runs on port 5000 by default.
if __name__ == '__main__':
    print("Starting!")
    app.run(debug=False, host='0.0.0.0',port=80)