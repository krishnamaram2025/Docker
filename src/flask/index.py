from flask import Flask, request, render_template
from flask_mysqldb import MySQL
application = Flask(__name__)

import os
MYSQL_HOST = os.environ['MYSQL_HOST']

#configure db
application.config['MYSQL_HOST'] = MYSQL_HOST
application.config['MYSQL_USER'] = 'krishna'
application.config['MYSQL_PASSWORD'] = 'Krishna_123'
application.config['MYSQL_DB'] = 'indigo'
mysql = MySQL(application)

@application.route('/')
def selectdata():
       cur = mysql.connection.cursor()
       cur.execute('select * from student')
       data = cur.fetchall()
       return render_template('index.html', msg=data)
if __name__ == '__main__':
    application.run(port=5001)


