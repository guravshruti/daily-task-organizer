import streamlit as st

st.set_page_config(page_title="Superman Task Tracker", page_icon="🦸‍♂️")
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0b3d91, #001f54);
    color: white !important;
}

/* Make ALL normal text white */
p, div, span, label {
    color: white !important;
}

/* Title */
h1 {
    text-align: center;
    color: #FFD700 !important;
    text-shadow: 2px 2px 8px black;
}

/* Subheaders */
h2, h3 {
    color: #00BFFF !important;
}

/* Input text */
input {
    color: red !important;
}

/* Checkbox text */
div[data-testid="stCheckbox"] label {
    color: white !important;
}

/* Buttons */
div.stButton > button {
    background-color: #e10600;
    color: white !important;
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
st.title("🦸‍♂️ Superman Daily Mission Tracker")
st.write("Plan your missions. Conquer your day like a hero.")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add new task
# Add new task

if "mission_input" not in st.session_state:
    st.session_state.mission_input = ""

new_task = st.text_input("Add a new mission", key="mission_input")

if st.button("Add Mission"):
    if new_task:
        st.session_state.tasks.append({
            "task": new_task,
            "completed": False
        })
        st.session_state.mission_input = ""
        st.rerun()   # 🔥 This refreshes safely
    else:
        st.warning("Enter a mission first!")
st.write("---")

# Display tasks
st.subheader("Today's Missions")

completed = []
incompleted = []

for i, task_data in enumerate(st.session_state.tasks):
    checked = st.checkbox(task_data["task"], value=task_data["completed"], key=i)
    st.session_state.tasks[i]["completed"] = checked

    if checked:
        completed.append(task_data["task"])
    else:
        incompleted.append(task_data["task"])

st.write("---")
if st.button("Mission Report"):

    st.subheader("✅ Missions Accomplished")
    if completed:
        for task in completed:
            st.write("🟢 " + task)
        st.success("Outstanding work, Hero! 💪🔥")
    else:
        st.info("No missions completed yet.")

    st.subheader("❌ Pending Missions")
    if incompleted:
        for task in incompleted:
            st.write("🔴 " + task)
        st.warning("Finish these and save the day! 🦸‍♂️")
    else:
        st.balloons()
        st.success("All missions completed! The world is safe! 🌍✨")
  




