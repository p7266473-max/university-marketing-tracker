import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="University Marketing Campaign Tracker",
    page_icon="🎓",
    layout="wide",
)

st.markdown('''
<style>
thead tr th { background: linear-gradient(135deg, #6c63ff, #3b82f6) !important; color: white !important; }
tbody tr:hover td { background: rgba(99,102,241,0.15) !important; }
</style>
''', unsafe_allow_html=True)

st.title("🎓 University Staff Marketing Campaign Tracker")
st.markdown("**Weekly social media tracking across Facebook, Instagram, Telegram, WhatsApp, and LinkedIn.**")
st.divider()

STAFF = ["Dr. Sarah Ahmed", "Prof. James Lim", "Ms. Priya Nair", "Mr. David Osei", "Dr. Layla Hassan", "Mr. Kevin Tan"]
PLATFORMS = ["Facebook", "Instagram", "Telegram", "WhatsApp", "LinkedIn"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
STATUS_OPTS = ["✅ Posted", "⏳ Scheduled", "❌ Missed"]

if "df" not in st.session_state:
    rows = []
    for staff in STAFF:
        for day in DAYS[:5]:
            platform = random.choice(PLATFORMS)
            rows.append({
                "Staff Name": staff,
                "Day": day,
                "Platform": platform,
                "Post Topic": f"{platform} campaign by {staff.split()[1]}",
                "Status": random.choice(STATUS_OPTS),
            })
    st.session_state.df = pd.DataFrame(rows)

df = st.session_state.df

col1, col2, col3, col4 = st.columns(4)
col1.metric("👥 Total Staff", len(STAFF))
col2.metric("📊 Total Posts", len(df))
col3.metric("✅ Posted", len(df[df["Status"] == "✅ Posted"]))
col4.metric("❌ Missed", len(df[df["Status"] == "❌ Missed"]))

st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["📋 Weekly Activity Log", "👤 By Staff Member", "📱 Platform Breakdown", "➕ Log New Post"])

with tab1:
    st.subheader("Weekly Activity Schedule")
    st.dataframe(df, use_container_width=True, height=400)

with tab2:
    st.subheader("Staff Reports")
    selected_staff = st.selectbox("Select Staff Member", df["Staff Name"].unique())
    staff_df = df[df["Staff Name"] == selected_staff]
    st.metric("Total Posts Logged", len(staff_df))
    st.dataframe(staff_df, use_container_width=True)

with tab3:
    st.subheader("Platform Distribution")
    p_counts = df["Platform"].value_counts().reset_index()
    p_counts.columns = ["Platform", "Count"]
    st.bar_chart(p_counts.set_index("Platform"))

with tab4:
    st.subheader("Log New Campaign Post")
    with st.form("new_post"):
        s_name = st.selectbox("Staff Name", STAFF)
        plat = st.selectbox("Platform", PLATFORMS)
        d_day = st.selectbox("Day", DAYS)
        topic = st.text_input("Post Topic")
        stat = st.selectbox("Status", STATUS_OPTS)
        if st.form_submit_button("📌 Submit Post") and topic:
            new_r = pd.DataFrame([{"Staff Name": s_name, "Day": d_day, "Platform": plat, "Post Topic": topic, "Status": stat}])
            st.session_state.df = pd.concat([st.session_state.df, new_r], ignore_index=True)
            st.success(f"Logged post for {s_name} on {plat}!")

st.divider()
st.caption("University Marketing Campaign Tracker • Streamlit • AGY2")
