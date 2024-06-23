from flask import Flask
import pymysql.cursors

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def  Person(name):
    return name

@app.route("/database/<id>")
def database(id):
    user = None
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='School3',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `students` (`first_name`, `last_name`) VALUES (%s, %s)"
            cursor.execute(sql, ('Alice', 'Jane'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    return id



if __name__ == "__main__":
    app.run(debug=True)
    