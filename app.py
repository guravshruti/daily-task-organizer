import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Superman Mission",
    page_icon="🦸‍♂️",
    layout="centered"
)
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
    color: white !important;
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


# ---------- Session State (No JSON Needed) ----------
if "streak" not in st.session_state:
    st.session_state.streak = 0
    st.session_state.last_date = ""

st.title("🦸‍♂️ Superman Daily Mission")

st.markdown("""
<div class="mission-box">
<strong>Today's Mission:</strong><br>
✔ Stay disciplined<br>
✔ Finish your tasks<br>
✔ Train like a hero<br>
✔ Win the day
</div>
""", unsafe_allow_html=True)

st.markdown("## 🔥 Current Streak")
st.markdown(f"<div class='big-number'>{st.session_state.streak} Days</div>", unsafe_allow_html=True)

if st.button("Mission Completed ✅"):
    today = str(date.today())

    if st.session_state.last_date != today:
        st.session_state.streak += 1
        st.session_state.last_date = today
        st.success("Power Level Increased 💪")




    

 






  




