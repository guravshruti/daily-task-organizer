import streamlit as st
import json
import os
from datetime import date

st.set_page_config(
    page_title="Superman Mission",
    page_icon="🦸‍♂️",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>

/* Remove all extra padding */
.block-container {
    padding-top: 0.5rem;
    padding-bottom: 0rem;
}

/* Remove gap between elements */
div[data-testid="stVerticalBlock"] > div {
    gap: 0rem;
}

/* Background */
.stApp {
    background: linear-gradient(to bottom, #0b0f2b, #1a1f4f);
    color: white;
}

/* Title */
h1 {
    color: #FFD700;
    font-size: 42px;
    margin-bottom: 0px;
}

/* Subheaders */
h2 {
    color: #00BFFF;
    font-size: 28px;
    margin-top: 5px;
    margin-bottom: 5px;
}

/* Streak number */
.big-number {
    font-size: 48px;
    font-weight: bold;
    color: #FFD700;
    margin-top: -5px;
    margin-bottom: 5px;
}

/* Mission box */
.mission-box {
    background-color: #11163a;
    padding: 12px;
    border-radius: 10px;
    border: 2px solid #FFD700;
    font-size: 18px;
    margin-bottom: 8px;
}

/* Button */
.stButton > button {
    font-size: 18px;
    font-weight: bold;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Data ----------
DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"streak": 0, "last_date": ""}, f)

with open(DATA_FILE, "r") as f:
    data = json.load(f)

# ---------- Title ----------
st.title("🦸‍♂️ Superman Daily Mission")

# ---------- Mission ----------
st.markdown("""
<div class="mission-box">
<strong>Today's Mission:</strong><br>
✔ Stay disciplined<br>
✔ Finish your tasks<br>
✔ Train like a hero<br>
✔ Win the day
</div>
""", unsafe_allow_html=True)

# ---------- Streak ----------
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

        st.success("Power Level Increased 💪")






