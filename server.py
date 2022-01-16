from flask import Flask, render_template # importing Flask

app = Flask(__name__) # creating a Flask object

@app.route('/') # associating route with '/'
def home(): # default output

    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'},
    ]

    return render_template("index.html", users = users)

if __name__ == "__main__":
    app.run(debug=True)