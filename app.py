import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Superman Mission",
    page_icon="🦸‍♂️",
    layout="centered"
)

# ---------- Style ----------
st.markdown("""
<style>
header {visibility: hidden;}
footer {visibility: hidden;}

.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
}

.stApp {
    background: linear-gradient(to bottom, #0b0f2b, #1a1f4f);
    color: white;
}

h1 {
    color: #FFD700;
    font-size: 48px;
    text-align: center;
}

.mission-box {
    background-color: #11163a;
    padding: 15px;
    border-radius: 12px;
    border: 2px solid #FFD700;
    font-size: 20px;
    margin-bottom: 10px;
}

.big-number {
    font-size: 52px;
    font-weight: bold;
    color: #FFD700;
    text-align: center;
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




    

 






  




