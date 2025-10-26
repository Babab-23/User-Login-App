from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
db_config={
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "flask_users"
}
@app.route("/login",methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST" and "username" and "password" in request.form:
        username=request.form["username"]
        password=request.form["password"]
        mydb=mysql.connector.connect(** db_config)
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails Where Name= %s and Passwrd=%s"),((username,password))
        account=mycursor.fecthone()  
        if account:
            name=account[1]     
            id=account[0]  
            msg="Logged in Successfully"   
            return render_template("index.html",msg=msg,name=name,id=id) 
        else:
            msg="Incorrect Credentials. Kindly Check"      
            return render_template("login.html",msg=msg)
@app.route("/register",methods=["GET","POST"])
def login():
    msg=""
    if request.method=="POST" and "username" and "password" in request.form and "email" in request.form:
        username=request.form["username"]
        password=request.form["password"]
        email=request.form["email"]
        mydb=mysql.connector.connect(** db_config)
        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails Where Name= %s and Passwrd=%s"),((username,password))
        account=mycursor.fecthone()  
        if account:
            msg="Account already exists!"
        else:
            mycursor.execute("INSERT INTO LoginDeatails(Name,Password,Email)VALUES(%s,%s,%s)",(username,password,email))
            mydb.commit()
            msg="You have successfully registered!"
        mycursor.close()
        mydb.close()
        return render_template("login.html",msg=msg)
    return render_template("register.html",msg=msg)
@app.route("/login")
def logout():
    name=""
    id=""
    msg="Logged out successfully!"
    return render_template("login.html",msg=msg,name=name,id=id)
@app.route("/")
def home():
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)                                                                     