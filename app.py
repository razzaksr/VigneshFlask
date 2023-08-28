from flask import Flask,make_response, render_template

app=Flask(__name__)

@app.route("/")
def helloThere():
    return make_response("<h1>I am a Full stack professional</h1>")

@app.route("/components")
def askMe():
    return make_response(
        "<ol type='I'><li>Jinja</li><li>WSGI</li><li>pymongo</li></ol>")

@app.route("/page1")
def tempFirst():
    return render_template("first.html")

if __name__=="__main__":
    app.run(debug=True,port=1111)