import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ================= CLEAR ONLY DONORS =================
cursor.execute("DELETE FROM donors")


def date_days_ago(days):
    return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")


donors = [

    # ================= A+ =================
    ("Arun", "A+", "9001234567", "Madurai", "625001", date_days_ago(120)),
    ("Karthik", "A+", "9002234567", "Chennai", "600001", date_days_ago(200)),
    ("Vijay", "A+", "9003234567", "Coimbatore", "641001", date_days_ago(50)),
    ("Ajay", "A+", "9004234567", "Salem", "636001", date_days_ago(300)),
    ("Suresh", "A+", "9005234567", "Trichy", "620001", date_days_ago(400)),
    ("Bala", "A+", "9006234567", "Madurai", "625002", date_days_ago(30)),
    ("Prakash", "A+", "9007234567", "Chennai", "600002", date_days_ago(180)),

    # ================= A- ================= (5 NOT eligible)
    ("Arunraj", "A-", "9011234567", "Coimbatore", "641002", date_days_ago(10)),
    ("Kavin", "A-", "9012234567", "Madurai", "625003", date_days_ago(20)),
    ("Ravi", "A-", "9013234567", "Trichy", "620002", date_days_ago(30)),
    ("Vignesh", "A-", "9014234567", "Salem", "636002", date_days_ago(40)),
    ("Mani", "A-", "9015234567", "Chennai", "600003", date_days_ago(60)),

    ("Dinesh", "A-", "9016234567", "Madurai", "625004", date_days_ago(120)),
    ("Saravanan", "A-", "9017234567", "Coimbatore", "641003", date_days_ago(150)),

    # ================= B+ =================
    ("Senthil", "B+", "9021234567", "Madurai", "625001", date_days_ago(10)),
    ("Murugan", "B+", "9022234567", "Chennai", "600004", date_days_ago(20)),
    ("Ramesh", "B+", "9023234567", "Coimbatore", "641004", date_days_ago(400)),
    ("Gopi", "B+", "9024234567", "Salem", "636003", date_days_ago(15)),
    ("Kumar", "B+", "9025234567", "Trichy", "620003", date_days_ago(500)),
    ("Arul", "B+", "9026234567", "Madurai", "625005", date_days_ago(80)),

    # ================= B- =================
    ("Vel", "B-", "9031234567", "Madurai", "625006", date_days_ago(100)),
    ("Manoj", "B-", "9032234567", "Chennai", "600006", date_days_ago(200)),
    ("Saravanan", "B-", "9033234567", "Coimbatore", "641005", date_days_ago(30)),
    ("Karthi", "B-", "9034234567", "Salem", "636004", date_days_ago(40)),
    ("Raja", "B-", "9035234567", "Trichy", "620004", date_days_ago(300)),
    ("Muthu", "B-", "9036234567", "Madurai", "625007", date_days_ago(500)),
    ("Sakthi", "B-", "9037234567", "Chennai", "600007", date_days_ago(600)),

    # ================= O+ =================
    ("Rajesh", "O+", "9041234567", "Coimbatore", "641006", date_days_ago(10)),
    ("Kannan", "O+", "9042234567", "Madurai", "625008", date_days_ago(200)),
    ("Mohan", "O+", "9043234567", "Chennai", "600008", date_days_ago(50)),
    ("Manoj", "O+", "9044234567", "Salem", "636005", date_days_ago(120)),
    ("Arvind", "O+", "9045234567", "Trichy", "620005", date_days_ago(300)),
    ("Bharath", "O+", "9046234567", "Madurai", "625009", date_days_ago(40)),
    ("Sathish", "O+", "9047234567", "Chennai", "600009", date_days_ago(600)),

    # ================= O- =================
    ("Omkar", "O-", "9051234567", "Coimbatore", "641007", date_days_ago(15)),
    ("Praveen", "O-", "9052234567", "Madurai", "625010", date_days_ago(25)),
    ("Naveen", "O-", "9053234567", "Chennai", "600010", date_days_ago(35)),
    ("Dinesh", "O-", "9054234567", "Salem","636005", date_days_ago(120)),
    ("Raja", "O-", "9055234567", "Trichy","620005", date_days_ago(200)),
    ("Kumar", "O-", "9056234567", "Madurai", "625009",date_days_ago(300)),
    ("Vimal", "O-", "9057234567", "Chennai", "600009",date_days_ago(400)),

    # ================= AB+ =================
    ("Arun AB", "AB+", "9061234567", "Coimbatore", "641008", date_days_ago(10)),
    ("Kavin AB", "AB+", "9062234567", "Madurai", "625012", date_days_ago(200)),
    ("Vijay AB", "AB+", "9063234567", "Chennai", "600012", date_days_ago(50)),
    ("Ajay AB", "AB+", "9064234567", "Salem", "636005",date_days_ago(120)),
    ("Suresh AB", "AB+", "9065234567", "Trichy","620005", date_days_ago(300)),
    ("Bala AB", "AB+", "9066234567", "Madurai","625009", date_days_ago(40)),
    ("Prakash AB", "AB+", "9067234567", "Chennai","600009", date_days_ago(600)),

    # ================= AB- =================
    ("Arun AB-", "AB-", "9071234567", "Coimbatore", "641009", date_days_ago(15)),
    ("Kavin AB-", "AB-", "9072234567", "Madurai", "625014", date_days_ago(25)),
    ("Vijay AB-", "AB-", "9073234567", "Chennai", "600014", date_days_ago(35)),
]

cursor.executemany("""
INSERT INTO donors(name, blood, phone, location, pincode, last_donation)
VALUES (?,?,?,?,?,?)
""", donors)

conn.commit()
conn.close()

print("Seed updated (ALL tables ready, eligibility meaningful)")