from flask import Flask, render_template

app = Flask(__name__)

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