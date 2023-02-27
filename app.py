# import sqlite3
# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def submit_form():
#     # Get the data from the HTML form

#     name = request.form['name']
#     email = request.form['email']
#     message = request.form['message']

#     # Store the data in a SQLite database
#     conn = sqlite3.connect('mydatabase.db')
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO submissions (name, email, message) VALUES (?, ?, ?)', (name, email, message))
#     conn.commit()
#     conn.close()

#     # Return a success message to the user
#     return 'Thank you for submitting the form'

# if __name__ == '__main__':
#     app.run()


# from flask import Flask, render_template, request
# import uuid

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/form.html', methods=['POST'])
# def submit():

#     x = str(uuid.uuid4())[0:15]

#     name = request.form['name']
#     email = request.form['email']
#     message = request.form['message']
#     # Do something with the data (e.g. save it to a database)
#     return 'Thank you for your submission, {}!'.format(name)

# if __name__ == '__main__':
#     app.run()


# import mysql.connector
# from mysql.connector import errorcode
# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/form.html', methods=['POST'])
# def store_data():
#     # Get the form data

#     name = request.form['name']
#     email = request.form['email']

#     # Connect to the database
#     try:
#         cnx = mysql.connector.connect(user='your_username', password='your_password',
#                                       host='your_host', database='your_database')
#         cursor = cnx.cursor()

#         # Create the table if it doesn't exist
#         table_name = 'users'
#         create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
#         cursor.execute(create_table_query)

#         # Insert the data into the table
#         insert_data_query = f"INSERT INTO {table_name} (name, email) VALUES (%s, %s)"
#         data = (name, email)
#         cursor.execute(insert_data_query, data)

#         cnx.commit()
#         cursor.close()
#         cnx.close()

#         return redirect('/success.html')

#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             return "Something is wrong with your username or password"
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             return "Database does not exist"
#         else:
#             return f"Error: {err}"


from flask import Flask ,render_template, request 
import sqlite3
import os
import uuid

currentdirectory = os.path.dirname(os.path.abspath(__file__))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/form.html",methods=["POST"])
def data():
    id = str(uuid.uuid4())[0:15]

    
    date = request.form['date']
    place = request.form['place']
    name = request.form['name']
    gender = request.form['gender']
    cheif_complaint = request.form['complaint']
    past_medical_history = request.form['history']
    past_dental_visit = request.form['visit']
    personal_habits = request.form.getlist('habits')
    tooth_number = request.form['toothnumber']
    decayed = request.form['decayed']
    missing = request.form['missing']
    filled = request.form['filled']
    pain = request.form['pain']
    fractured = request.form['fractured']
    mobility = request.form['mobility']
    others = request.form['others']
    gingiva = request.form['gingiva']
    description = request.form['comment']
    dental_fluorosis = request.form['floro']
    malocclusion = request.form['malo']
    oral_muscosal_lesion = request.form['masc']
    condition = request.form['condition']
    location = request.form['location']
    treatment_done = request.form['treatment']
    expalnation = request.form['explanation']


    conn = sqlite3.connect('example.db') # create a database if it does not exist
    c = conn.cursor()

    # create a table if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS Patients
                 (Patient_id TEXT,dateofvisit TEXT,place TEXT,name_of_patient TEXT,gender TEXT,cheif_complaint TEXT,past_medical_history TEXT,past_dental_visit TEXT,personal_habits TEXT,tooth_number INTEGER,decayed_tooth INTEGER,missing_tooth INTEGER,filled_tooth INTEGER,pain_in_tooth INTEGER,fractured_tooth INTEGER,mobility_tooth INTEGER,others TEXT,gingiva TEXT,description TEXT,dental_fluorosis TEXT, malocclusion TEXT,oral_muscosal_lesion TEXT,condition TEXT,treatment_done TEXT,expalnation TEXT)''')

    # insert data into the table
    c.execute("INSERT INTO Patients VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id,date,place,name,gender,cheif_complaint,past_medical_history,past_dental_visit,personal_habits,tooth_number,decayed,missing,filled,pain,fractured,mobility,others,gingiva,description,dental_fluorosis,malocclusion,oral_muscosal_lesion,condition,treatment_done,expalnation))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
    

