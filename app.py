import requests
import request
import random
from flask import Flask,render_template,redirect, url_for, request, session
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    # global s
    if request.method == "POST":
        myDict = request.form  
        s1 = float(myDict['s1'])
        if (s1 < 10):
            link="https://www.youtube.com/watch?v=OGgG4nH8vOo&t=19s+%28carnival+A%2719%29"
            # s=666
        elif(s1<20):
            link="https://www.youtube.com/watch?v=34eDWAL8dIM&t=88s+%28Main+Video+A%2719%29"
            # s=456
        elif(s1<30):
            link = "https://www.instagram.com/tv/B9eMFXcjFOk/?igshid=wu6az47qkhs2"
            # s=787
        elif(s1<40):
            link ="https://www.instagram.com/tv/B-R1nj9jl1z/?igshid=1a8481gk62q5r"
            # s=385
        elif(s1<50):
            link ="https://www.instagram.com/p/B9s86BDjgZM/?igshid=15pcz98zt8b8i"
            # s=65 
        elif(s1<60):
            link ="https://www.instagram.com/p/B-juME0DGEP/?igshid=xzs9qzvnm9f4"
            # s=143 
        elif(s1<70):
            link ="https://www.instagram.com/p/B-jGO0ZDohX/?igshid=1ktqlefhsp1pp"
            # s=982 
        elif(s1<80):
            link ="https://www.instagram.com/p/B-hhuPGjWIF/?igshid=97ru6fhnly1l"
            # s=369
        elif(s1<90):
            link ="https://www.instagram.com/p/B-gnCQ6jlw4/?igshid=17n06e6hhsbq4"
            # s=211 
        elif(s1<100):
            link ="https://www.instagram.com/p/B-RbgWJjrNf/?igshid=17ifv17lwdkk1"
            # s=420  
        else:
            return render_template('wrong.html')
        return render_template('quiz1.html',link=link)
    return render_template('index.html')



@app.route('/check',methods=["GET", "POST"])
def check():
    #global n
    if request.method == "POST":
        myDict2 = request.form  
        s = int(myDict2['s'])
        # return render_template('quiz2.html',s=s)
        if (s==666 or s==456 or s==787 or s==385 or s==65 or s==143 or s== 982 or s==369 or s==211 or s==420):
            session['n'] = random.randint(1,10)
            return render_template('quiz2.html',num=session['n'],s=s)
        else:
            return render_template('wrong2.html')
    # return render_template('wrong.html')



@app.route('/final',methods=["GET", "POST"])
def about():
    if request.method == "POST":
        myDict = request.form  
        s2 = myDict['s2']
        n = session['n']
        if (n==1 and s2 =="31"):
            session.pop('n', None)
            return render_template('yay.html')
        elif(n==2 and s2 == "7"):
            session.pop('n', None)
            return render_template('yay.html')
        elif((n==3 and s2 == "Y") or (n==3 and s2 == "y")):
            session.pop('n', None)
            return render_template('yay.html')
        elif(n==4 and s2 == "5"):
            session.pop('n', None)
            return render_template('yay.html')
        elif((n==5 and s2 == "C") or (n==5 and s2 == "c")):
            session.pop('n', None)
            return render_template('yay.html')  
        elif(n==6 and s2 == "2"):
            session.pop('n', None)
            return render_template('yay.html')
        elif(n==7 and s2 == "18"):
            session.pop('n', None)
            return render_template('yay.html')
        elif(n==8 and s2 == "3"):
            session.pop('n', None)
            return render_template('yay.html')
        elif(n==9 and s2 == "36"):
            session.pop('n', None)
            return render_template('yay.html')
        elif(n==10 and s2 == "6"):
            session.pop('n', None)
            return render_template('yay.html')
        else:
            return render_template('wrong.html')

# @app.errorhandler(404)
# def not_found(e):
#     return render_template("wrong2.html") 

# @app.errorhandler(500)
# def not_found(e):
#     return render_template("wrong2.html")

app.secret_key = "gaius-dev"

if __name__ == '__main__':
    app.run(debug=True)