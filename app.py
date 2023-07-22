from flask import Flask, render_template, request, redirect, jsonify,url_for, session
import mysql.connector
#from passlib.hash import sha256_crypt
app = Flask(__name__)



# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin",
    database="hospitallogin"
)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login', methods =['GET', 'POST'])
def log():
    msg = ''
    msg2=''
    if request.method == 'POST' and 'login-email' in request.form and 'login-password' in request.form:
        email = request.form['login-email']
        password = request.form['login-password']
        
        cursor = db.cursor()
        cursor.execute('SELECT email,password FROM reg WHERE email = %s AND password = %s', (email, password ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            #session['id'] = account['id']
            session['email'] = account['email']
            session['password'] = account['password']
            return 'Logged in successfully !'
            #return render_template('home.html', msg = msg)
        else:
            #msg2 = 'Incorrect username / password !'
            return 'Incorrect username / password !'
            #return render_template('login.html', msg2=msg2)


@app.route('/register')
def Registration():
    return render_template('Registration.html')

@app.route('/register', methods= ['GET' , 'POST'])
def submit():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    phonenumber=request.form['phonenumber']
    address=request.form['address']
    password=request.form['password']
    #encpassword=sha256_crypt.hash(password)

    # Insert data into the database
    cursor = db.cursor()
    query = "INSERT INTO reg (firstname,lastname,email,phonenumber,address,password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (firstname,lastname,email,phonenumber,address,password)
    cursor.execute(query, values)
    db.commit()

    # Optionally, you can close the database connection after the insertion
    cursor.close()
    db.close()
   
    #return "Data inserted Successfully"
    return render_template('login.html')

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/contact')

def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
   return render_template('about.html')

#@app.route('/contact', methods= ['GET' , 'POST'])
#def submit():
#    name  = request.form['name'] 
#    email = request.form['email']
#    phonenumber=request.form['phonenumber']
#    desc=request.form['desc']

    # Insert data into the database
#    cursor = db.cursor()
#    query = "INSERT INTO reg (name,email,phonenumber,desc) VALUES (%s, %s, %s, %s)"
#    values = (name,email,phonenumber,desc)
#    cursor.execute(query, values)
#    db.commit()

    # Optionally, you can close the database connection after the insertion
#    cursor.close()
#    db.close()
   
    #return "Data inserted Successfully"
#    return render_template('Data_submit.html')

#

@app.route('/chat')
def chat():
   return render_template('chatbot.html');
 
if __name__ == '__main__':
    app.run(debug=True)
