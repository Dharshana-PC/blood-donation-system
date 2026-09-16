// ================= DONOR REGISTRATION =================
async function registerDonor() {

    try {
        await fetch("http://127.0.0.1:5000/donor", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: donor_name.value,
                blood: donor_blood.value,
                phone: donor_phone.value,
                location: donor_location.value,
                pincode: donor_pincode.value,
                last_donation: donor_date.value
            })
        });

        alert("Donor Registered Successfully");

    } catch (err) {
        console.log(err);
        alert("Error registering donor");
    }
}


// ================= PATIENT REGISTRATION (STEP FLOW FIXED) =================
async function registerPatient() {

    await fetch("http://127.0.0.1:5000/patient", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: patient_name.value,
            blood: patient_blood.value,
            phone: patient_phone.value,
            location: patient_location.value,
            pincode: patient_pincode.value
        })
    });

    alert("Patient Registered Successfully");

    // 🔥 SHOW SEARCH
    document.getElementById("registerSection").style.display = "none";
    document.getElementById("searchSection").style.display = "block";
}


// ================= SEARCH DONORS (KNN) =================
async function searchDonors() {

    try {
        const res = await fetch("http://127.0.0.1:5000/search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                blood: blood.value,
                pincode: pincode.value
            })
        });

        const donors = await res.json();

        let out = "";

        if (donors.length === 0) {
            out = "<div class='card'>No Donors Found</div>";
        }

        donors.forEach(d => {
            out += `
                <div class="card">
                    <h3>${d.name}</h3>
                    <p><b>Blood:</b> ${d.blood}</p>
                    <p><b>Phone:</b> ${d.phone}</p>
                    <p><b>Location:</b> ${d.location}</p>

                    <button onclick="chooseDonor('${d.name}','${d.blood}','${d.phone}')">
                        Choose Donor
                    </button>
                </div>
            `;
        });

        results.innerHTML = out;

    } catch (err) {
        console.log(err);
    }
}


// ================= CHOOSE DONOR =================
async function chooseDonor(name, blood, phone) {

    let patient = prompt("Enter patient name");

    try {
        await fetch("http://127.0.0.1:5000/choose", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                donor_name: name,
                patient_name: patient,
                blood: blood,
                phone: phone
            })
        });

        alert("Donor Selected Successfully");

    } catch (err) {
        console.log(err);
    }
}


// ================= ADMIN LOGIN + GROUPED TABLES =================
async function adminLogin() {

    const u = username.value;
    const p = password.value;

    if (u !== "admin" || p !== "admin123") {
        alert("Invalid Login");
        return;
    }

    const donors = await fetch("http://127.0.0.1:5000/all_donors").then(r => r.json());
    const patients = await fetch("http://127.0.0.1:5000/all_patients").then(r => r.json());
    const chosen = await fetch("http://127.0.0.1:5000/chosen").then(r => r.json());

    const groups = {
        "A+": [], "A-": [],
        "B+": [], "B-": [],
        "O+": [], "O-": [],
        "AB+": [], "AB-": []
    };

    donors.forEach(d => {
        if (groups[d.blood]) {
            groups[d.blood].push(d);
        }
    });

    let out = "<h2>Donors (Grouped by Blood Type)</h2>";

    for (let g in groups) {

        out += `<h3>${g}</h3>`;
        out += `<table class="table">`;
        out += `<tr><th>Name</th><th>Phone</th><th>Location</th></tr>`;

        groups[g].forEach(d => {
            out += `
                <tr onclick="this.classList.toggle('selected')">
                    <td>${d.name}</td>
                    <td>${d.phone}</td>
                    <td>${d.location}</td>
                </tr>
            `;
        });

        out += `</table>`;
    }

    // PATIENT TABLE
    out += "<h2>Patients</h2>";
    out += "<table class='table'><tr><th>Name</th><th>Blood</th><th>Phone</th><th>Location</th></tr>";

    patients.forEach(p => {
        out += `
            <tr>
                <td>${p.name}</td>
                <td>${p.blood}</td>
                <td>${p.phone}</td>
                <td>${p.location}</td>
            </tr>
        `;
    });

    out += "</table>";

    // CHOSEN TABLE
    out += "<h2>Chosen Donors</h2>";
    out += "<table class='table'><tr><th>Donor</th><th>Patient</th><th>Blood</th><th>Phone</th></tr>";

    chosen.forEach(c => {
        out += `
            <tr>
                <td>${c.donor_name}</td>
                <td>${c.patient_name}</td>
                <td>${c.blood}</td>
                <td>${c.phone}</td>
            </tr>
        `;
    });

    out += "</table>";

    adminResults.innerHTML = out;
}