from flask import Flask,make_response, render_template, request

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

@app.route("/skills")
def showTable():
    myList=[
        {"front":"Thymeleaf","back":"SpringBoot","data":"Oracle","server":"apache tomcat"},
        {"front":"Jinja","back":"Flask","data":"MongoDB","server":"WSGI"},
        {"front":"React","back":"DJango","data":"MySQL","server":"WSGI"},
        {"front":"Vite","back":"Express","data":"MongoDB","server":"Node"},
    ]
    return render_template("table.html",stack=myList)

@app.route("/repeat")
def callLoop():
    myList=['Spring Boot','Flask','DJnago','Node','Hibernate']
    return render_template("loops.html",myFrame=myList)

@app.route("/decide/<float:income>")
def decision(income):
    return render_template("decisionmakings.html",ctc=income)

@app.route("/jin/<int:value>")
def callJinja(value):
    return render_template("jinjacode.html",number=value);

@app.route("/currency/<int:dollar>")
def passFormats(dollar):
    rupees=dollar*82.77;
    return render_template("opted.html",var=rupees)

@app.route("/data/<thor>")
def passValue(thor):
    return render_template("opted.html",var=thor)

@app.route("/send",methods=['GET','POST'])
def performSignUp():
    if request.method=="GET":
        return render_template("bootforms.html")
    else:
        firstName=request.form['fname']
        lastName=request.form['lname']
        email=request.form['mail']
        contact=request.form['mobile']
        print(firstName,lastName,contact,email)
        return render_template("bootforms.html",msg=firstName+" account created")

# @app.route("/signup")
# def showSignUp():
#     return render_template("bootforms.html")


# @app.route("/send",methods=['POST'])
# def receiveSignUp():
#     firstName=request.form['fname']
#     lastName=request.form['lname']
#     email=request.form['mail']
#     contact=request.form['mobile']
#     print(firstName,lastName,contact,email)

if __name__=="__main__":
    app.run(debug=True,port=1111)