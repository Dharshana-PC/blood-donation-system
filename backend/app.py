from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from algorithms import find_best_donors

app = Flask(__name__)
CORS(app)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "Backend Running"


# ---------------- DONOR ----------------
@app.route("/donor", methods=["POST"])
def donor():
    data = request.json

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO donors(name,blood,phone,location,pincode,last_donation)
        VALUES(?,?,?,?,?,?)
    """, (
        data["name"], data["blood"], data["phone"],
        data["location"], data["pincode"], data["last_donation"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"msg": "donor saved"})


# ---------------- PATIENT ----------------
@app.route("/patient", methods=["POST"])
def patient():
    data = request.json

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO patients(name,blood,phone,location,pincode)
        VALUES(?,?,?,?,?)
    """, (
        data["name"], data["blood"], data["phone"],
        data["location"], data["pincode"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"msg": "patient saved"})


# ---------------- SEARCH (KNN - UNCHANGED ALGO) ----------------
@app.route("/search", methods=["POST"])
def search():
    data = request.json
    result = find_best_donors(data["blood"], data["pincode"])
    return jsonify(result)


# ---------------- ADMIN ----------------
@app.route("/all_donors")
def all_donors():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM donors")
    return jsonify([dict(r) for r in cur.fetchall()])


@app.route("/all_patients")
def all_patients():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    return jsonify([dict(r) for r in cur.fetchall()])


@app.route("/chosen")
def chosen():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM chosen")
    return jsonify([dict(r) for r in cur.fetchall()])


@app.route("/choose", methods=["POST"])
def choose():
    data = request.json

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO chosen(donor_name,patient_name,blood,phone)
        VALUES(?,?,?,?)
    """, (
        data["donor_name"],
        data["patient_name"],
        data["blood"],
        data["phone"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"msg": "saved"})


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from algorithms import find_best_donors

app = Flask(__name__)
CORS(app)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "Backend Running"


# ---------------- DONOR ----------------
@app.route("/donor", methods=["POST"])
def donor():
    data = request.json

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO donors(name,blood,phone,location,pincode,last_donation)
        VALUES(?,?,?,?,?,?)
    """, (
        data["name"], data["blood"], data["phone"],
        data["location"], data["pincode"], data["last_donation"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"msg": "donor saved"})


# ---------------- PATIENT ----------------
@app.route("/patient", methods=["POST"])
def patient():
    data = request.json

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO patients(name,blood,phone,location,pincode)
        VALUES(?,?,?,?,?)
    """, (
        data["name"], data["blood"], data["phone"],
        data["location"], data["pincode"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"msg": "patient saved"})


# ---------------- SEARCH (KNN - UNCHANGED ALGO) ----------------
@app.route("/search", methods=["POST"])
def search():
    data = request.json
    result = find_best_donors(data["blood"], data["pincode"])
    return jsonify(result)


# ---------------- ADMIN ----------------
@app.route("/all_donors")
def all_donors():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM donors")
    return jsonify([dict(r) for r in cur.fetchall()])


@app.route("/all_patients")
def all_patients():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    return jsonify([dict(r) for r in cur.fetchall()])


@app.route("/chosen")
def chosen():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM chosen")
    return jsonify([dict(r) for r in cur.fetchall()])


@app.route("/choose", methods=["POST"])
def choose():
    data = request.json

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO chosen(donor_name,patient_name,blood,phone)
        VALUES(?,?,?,?)
    """, (
        data["donor_name"],
        data["patient_name"],
        data["blood"],
        data["phone"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"msg": "saved"})


if __name__ == "__main__":
    app.run(debug=True)