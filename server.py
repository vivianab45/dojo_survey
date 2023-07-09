from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

#need this when putting data into sesstion
app.secret_key="secret"

# http://localhost:5000 - have this display a nice looking HTML form. 

@app.route('/')
def survey():
    

    return render_template("index.html")

# The form should be submitted to '/process'

@app.route('/process', methods=['POST'])
def process():
    print(request.form)

    session ['name']=request.form['name']
    session ['location']=request.form['location']
    session ['language']=request.form['language']
    session ['comment']=request.form['comment']

    
    return redirect('/result')


# http://localhost:5000/result - have this display HTML with the information that was submitted by POST
@app.route('/result')
def display():
    return render_template ("display.html")

# Reset form when Go Back button is clicked

@app.route('/reset')
def reset():
    session.clear()
    
    return redirect ('/')



if __name__=="__main__":
    app.run(debug=True)