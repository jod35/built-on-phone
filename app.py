from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

class DevConfig:
    SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = True
    DEBUG=True


app.config.from_object(DevConfig)
db=SQLAlchemy(app)




#modelzs

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(125),nullable=False)
    password=db.Column(db.String(125),nullable=False)




    def __repr__(self):
        return self.id

@app.route("/")
def index():
    users=User.query.all()
    return render_template('index.html',users=users)

@app.route("/about")
def about():
    return render_template('about.html')


#create a user
@app.route("/adduser",methods=["POST"])
def add_user():
    username=request.form.get('username')
    password=request.form.get('password')

    new_user=User(username=username,password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/")




app.run(debug=True)
