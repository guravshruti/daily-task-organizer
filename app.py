import streamlit as st
import json
import os
from datetime import date

# ---------- Page Config ----------
st.set_page_config(page_title="Superman Mission Tracker", page_icon="🦸‍♂️")

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #0b0f2b, #1a1f4f);
    color: white;
}

h1, h2, h3 {
    color: #FFD700;
}

.big-number {
    font-size: 40px;
    font-weight: bold;
    color: #00BFFF;
    margin-top: -15px;
}

.mission-box {
    background-color: #11163a;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #FFD700;
    color: white;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Data File ----------
DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"streak": 0, "last_date": ""}, f)

with open(DATA_FILE, "r") as f:
    data = json.load(f)

# ---------- Title ----------
st.title("🦸‍♂️ Superman Daily Mission")

# ---------- Mission Section ----------
st.subheader("🎯 Today's Mission")
st.markdown("""
<div class="mission-box">
✔ Be strong<br>
✔ Stay disciplined<br>
✔ Complete all tasks<br>
✔ Protect your goals like Superman
</div>
""", unsafe_allow_html=True)

# ---------- Decreased Space Before Streak ----------
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("🔥 Current Streak")

st.markdown(f"""
<div class="big-number">
{data['streak']} Days
</div>
""", unsafe_allow_html=True)

# ---------- Button ----------
if st.button("Mission Completed ✅"):
    today = str(date.today())

    if data["last_date"] != today:
        data["streak"] += 1
        data["last_date"] = today

        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

        st.success("Superman Power Increased! 💪")

    

 






  




