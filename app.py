import streamlit as st
import json
import os
from datetime import date

st.set_page_config(page_title="Superman Mission Tracker", page_icon="🦸‍♂️")

DATA_FILE = "data.json"

# ---------- LOAD DATA ----------
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {"tasks": [], "streak": 0, "last_completed": ""}

# ---------- SAVE FUNCTION ----------
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# ---------- SUPERHERO STYLE ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b3d91, #001f54);
    color: white;
}

h1 {
    text-align: center;
    color: #ffd700;
    text-shadow: 2px 2px 8px black;
}

div.stButton > button {
    background-color: #e10600;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #ff2a2a;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🦸‍♂️ SUPERMAN DAILY MISSION TRACKER")
st.markdown(f"### 📅 {date.today().strftime('%B %d, %Y')}")

st.write("Every day is a mission. Heroes don't quit.")

st.write("---")

# ---------- STREAK DISPLAY ----------
st.subheader(f"🔥 Current Streak: {data['streak']} Days")

st.write("---")

# ---------- ADD MISSION ----------
new_task = st.text_input("Add a new mission")

if st.button("🚀 Add Mission"):
    if new_task:
        data["tasks"].append({"task": new_task, "completed": False})
        save_data()
        st.success("Mission Added 🔥")
    else:
        st.warning("Enter a mission first!")

st.write("---")

# ---------- DISPLAY MISSIONS ----------
completed = []
incompleted = []

for i, task_data in enumerate(data["tasks"]):
    checked = st.checkbox(task_data["task"], value=task_data["completed"], key=i)
    data["tasks"][i]["completed"] = checked

    if checked:
        completed.append(task_data["task"])
    else:
        incompleted.append(task_data["task"])

save_data()

st.write("---")

# ---------- MISSION REPORT ----------
if st.button("📝 Mission Report"):

    st.subheader("✅ Missions Accomplished")

    if completed:
        for task in completed:
            st.write("🟢 " + task)

        today = str(date.today())

        if data["last_completed"] != today:
            data["streak"] += 1
            data["last_completed"] = today
            save_data()

        st.success("Outstanding Work, Hero! 💪🔥")

    else:
        st.info("No missions completed yet.")

    st.subheader("❌ Pending Missions")

    if incompleted:
        for task in incompleted:
            st.write("🔴 " + task)
    else:
        st.balloons()
        st.success("All missions completed! The world is safe 🌍✨")

# ---------- RESET ----------
st.write("---")

if st.button("🔄 Reset All Missions"):
    data["tasks"] = []
    save_data()
    st.success("New Day. New Power. New Missions. 💥")
