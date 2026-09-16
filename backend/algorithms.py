import sqlite3
import heapq
from datetime import datetime


# ================= ELIGIBILITY CHECK =================
def is_eligible(last_donation):

    try:
        last = datetime.strptime(last_donation, "%Y-%m-%d")
        days = (datetime.now() - last).days
        return days >= 90
    except:
        return False


# ================= HASHMAP GROUPING =================
def group_by_blood(donors):

    grouped = {}

    for d in donors:
        blood = d["blood"]

        if blood not in grouped:
            grouped[blood] = []

        grouped[blood].append(d)

    return grouped


# ================= KNN (DISTANCE CALCULATION) =================
def knn(donors, patient_pincode):

    for d in donors:
        try:
            d["distance"] = abs(int(d["pincode"]) - int(patient_pincode))
        except:
            d["distance"] = 999999

    donors.sort(key=lambda x: x["distance"])
    return donors


# ================= PRIORITY QUEUE (HEAP RANKING) =================
def priority_queue(donors):

    pq = []
    count = 0

    for d in donors:
        heapq.heappush(pq, (d["distance"], count, d))
        count += 1

    result = []

    while pq:
        result.append(heapq.heappop(pq)[2])

    return result


# ================= FINAL PIPELINE =================
def find_best_donors(blood, pincode):

    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM donors WHERE blood=?", (blood,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()

    # 1. ELIGIBILITY FILTER
    eligible = []
    for d in rows:
        if is_eligible(d["last_donation"]):
            eligible.append(d)

    # 2. HASHMAP (grouping step - used logically)
    grouped = group_by_blood(eligible)
    same_blood = grouped.get(blood, [])

    # 3. KNN (distance sorting)
    knn_result = knn(same_blood, pincode)

    # 4. PRIORITY QUEUE (final ranking)
    final_ranked = priority_queue(knn_result)

    return final_ranked[:5]