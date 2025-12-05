from flask import Flask, render_template
import mariadb

from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/annen')
def annen():
    return render_template("page2.html")

@app.route("/ping")
def ping():
    try:
        conn = get_db_connection()
        conn.close()
        return {"ok": True, "message": "Connected to MariaDB" }
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500

@app.route("/users")
def getUsers():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM prompts;"
        )
        messages = [row for row in cursor.fetchall()]
        conn.close()

        return messages
        

    except Exception as e:
        return {"ok": False, "error": str(e)}, 500


if __name__ == '__main__':
    app.run(debug=True)


