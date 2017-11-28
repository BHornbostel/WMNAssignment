from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def ind():
    return render_template("index.html")
@app.route("/process",methods=["POST"])
def submit():
    name = request.form['name']
    print name
    return redirect('/')
app.run(debug=True)