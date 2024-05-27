from flask import Flask, render_template, redirect, request, url_for, session, send_file
from flask_mysqldb import MySQL
import MySQLdb.cursors
# from flask_uploads import UploadSet, configure_uploads
import re
from datetime import datetime
import os 





app = Flask(__name__)

app.secret_key = 'key'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'portal'

# app.config['UPLOADED_PHOTOS_DEST'] = 'static/profile_pictures'
# photos = UploadSet('photos', extensions=['jpg', 'png', 'jpeg'])
# configure_uploads(app, photos)


# db = MySQL(app)
mysql = MySQL(app)

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(64), unique=True, nullable=False)
# 	email = db.Column(db.String(120), unique=True, nullable=False)
# 	profile_picture = db.Column(db.String(120), nullable=True)

# 	def __repr__(self):
#             return f'<User {self.username}>'



@app.route("/")
def index():
    return render_template('layout.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('layout.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        return redirect(url_for('result'))
    return render_template('result.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return redirect(url_for('about'))
    return render_template('about.html')
    
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        return redirect(url_for('update'))
    return render_template('update.html')


@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        return redirect(url_for('courses'))
    return render_template('courses.html')

@app.route('/assign', methods=['GET', 'POST'])
def assign():
    if request.method == 'POST':
        return redirect(url_for('assign'))
    return render_template('assign.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')


@app.route('/tec')
def tec():
    return render_template('tec.html')

@app.route('/attend', methods=['GET', 'POST'] )
def attend():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id,Fname, Lname FROM student")
    data = cur.fetchall()
    cur.close()
    return render_template('attend.html', data=data)

@app.route('/notify')
def notify():
    return render_template('notify.html')
     
 
@app.route('/register/admin', methods=['GET', 'POST'])
def admin_register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO reg VALUES (NULL, %s, %s, %s)', (username, password, email))
        mysql.connection.commit()
        msg = 'You have successfully registered!'
        return render_template('login.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('admin_register.html', msg=msg)



@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['Id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('admin_dashboard.html', msg = 'username')
        else:
            msg = 'Incorrect username / password !'
    return render_template('admin_login.html', msg = msg)


@app.route('/tec/login', methods=['GET', 'POST'])
def tec_login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM teacher WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['Id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('tec.html', msg = 'username')
        else:
            msg = 'Incorrect username / password !'
    return render_template('tec_login.html', msg = msg)


@app.route('/bursal/login', methods=['GET', 'POST'])
def bursal_login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM bursal WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['Id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('bursal_dashboard.html', msg = 'username')
        else:
            msg = 'Incorrect username / password !'
    return render_template('bursal_login.html', msg = msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM reg WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['Id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('user_dashboard.html', msg = 'username')
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)
 



@app.route('/register/user', methods=['GET', 'POST'])
def user_register():
    msg = ''
    if request.method == 'POST' and 'student' in request.form and 'parent' in request.form and 'former' in request.form and 'address' in request.form :
        student = request.form['student']
        parent = request.form['parent']
        former = request.form['former']
        address = request.form['address']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO enrol VALUES (NULL, %s, %s, %s, %s, %s)', (student, parent, former, address, datetime.now()))
        mysql.connection.commit()
        msg = 'You have successfully registered!'
        return render_template('login.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('user_register.html', msg=msg)

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)

    return redirect(url_for('home'))


@app.route('/')
@app.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Sname, Phonenum FROM admin")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM admin")
    admin_count = cur.fetchone()[0]
    cur.close()
    return render_template('admin.html', data=data, admin_count=admin_count)

@app.route('/teacher')
def teacher():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  Fname, Sname, Phonenum FROM teacher")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM teacher")
    teacher_count = cur.fetchone()[0]
    cur.close()
    return render_template('teacher.html', data=data, teacher_count=teacher_count)

@app.route('/student')
def student():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM student")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM student")
    student_count = cur.fetchone()[0]
    cur.close()
    return render_template('student.html', data=data, student_count=student_count)


@app.route('/study')
def study():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM student")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM student")
    student_count = cur.fetchone()[0]
    cur.close()
    return render_template('study.html', data=data, student_count=student_count)

@app.route('/stu')
def stu():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM stujss1")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM stujss1")
    stu_count = cur.fetchone()[0]
    cur.close()
    return render_template('stu.html', data=data, stu_count=stu_count)

@app.route('/stu1')
def stu_1():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM stujss2")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM stujss2")
    stu1_count = cur.fetchone()[0]
    cur.close()
    return render_template('stu.html', data=data, stu1_count=stu1_count)

@app.route('/stu2')
def stu_2():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM stujss3")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM stujss3")
    stu2_count = cur.fetchone()[0]
    cur.close()
    return render_template('stu.html', data=data, stu2_count=stu2_count)

@app.route('/stu3')
def stu_3():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM stuss1")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM stuss1")
    stu3_count = cur.fetchone()[0]
    cur.close()
    return render_template('stu.html', data=data, stu3_count=stu3_count)

@app.route('/stu4')
def stu_4():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM stuss2")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM stuss2")
    stu4_count = cur.fetchone()[0]
    cur.close()
    return render_template('stu.html', data=data, stu4_count=stu4_count)

@app.route('/stu5')
def stu_5():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Fname, Lname, Adminnum FROM stuss3")
    data = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM stuss3")
    stu5_count = cur.fetchone()[0]
    cur.close()
    return render_template('stu.html', data=data, stu5_count=stu5_count)

@app.route('/view/<int:id>')
def view(id):
    return f'Viewing row  with ID {id}'

@app.route('/modify/<int:id>')
def modify(id):
    return f'Modifying row  with ID {id}'

@app.route('/upload', methods=['POST'])
def upload_file():
    cursor = mysql.connection.cursor()
    file = request.files['file']
    cursor.execute('INSERT INTO files (name, data) VALUES(%s, %s)',(file.filename, file.read()))
    mysql.connection.commit()
    return '<h1> File uploaded successfully<h1>'

# @app.route('/update_profile_picture', methods=['POST'])
# def update_profile_picture():
# 	profile_picture = request.files['profile_picture']
# 	profile_picture.save(photos.path('profile_picture.jpg'))
	
# 	user = user.query.get((1))
# 	user.profile_picture = 'profile_picture.jpg'
# 	db.session.commit()
	
# 	return 'Profile picture updated successfully!', 200




if __name__ == '__main__':
    
    app.run(debug=True)