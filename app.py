from flask import Flask, render_template, request, jsonify
import mariadb
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/annen')
def annen():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)  # gir kolonnenavn som dict
        cursor.execute("SELECT * FROM prompts;")
        prompts = cursor.fetchall()
        conn.close()
        return render_template("page2.html", prompts=prompts)
    except Exception as e:
        return f"Error: {e}"

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
        cursor.execute("SELECT * FROM prompts;")
        messages = [row for row in cursor.fetchall()]
        conn.close()
        return messages
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500

# ----------------------------
# NY ROUTE: Generer svar
# ----------------------------
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    melding = data.get("melding", "")
    mottaker = data.get("mottaker", "")
    tone = data.get("tone", "")
    lengde = data.get("lengde", "")
    stil = data.get("stil", "")

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Hent et forslag som matcher mottaker, tone eller lengde, ikke eksakt melding
        cursor.execute(
            """
            SELECT forslag 
            FROM prompts 
            WHERE (mottaker LIKE %s OR tone LIKE %s OR lengde LIKE %s)
            ORDER BY RAND() 
            LIMIT 1
            """,
            (f"%{mottaker}%", f"%{tone}%", f"%{lengde}%")
        )
        row = cursor.fetchone()
        conn.close()

        if row:
            return jsonify({"forslag": row["forslag"]})
        else:
            return jsonify({"forslag": "Her er et generelt forslag: Hei! Jeg svarer straks på meldingen din."})

    except Exception as e:
        return jsonify({"forslag": f"Error: {e}"})


if __name__ == '__main__':
    app.run(debug=True)


