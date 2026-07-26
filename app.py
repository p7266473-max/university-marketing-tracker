import streamlit as st
import pandas as pd

# Add nostalgic styling
st.markdown("""
<style>
    /* Warm, nostalgic palette */
    :root {
        --bg-color: #fcfbf7;
        --text-color: #3e3a35;
        --accent-color: #8b5e3c;
        --table-header: #dcd0c0;
    }
    
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-color);
        font-family: 'Georgia', serif;
    }
    
    h1, h2, h3 {
        color: var(--accent-color);
        font-family: 'Georgia', serif;
        border-bottom: 2px solid var(--accent-color);
        padding-bottom: 0.5rem;
    }
    
    .stDataFrame {
        border: 1px solid var(--table-header);
    }
    
    /* Subtle polish */
    .stButton>button {
        background-color: var(--accent-color);
        color: white;
        border: none;
        border-radius: 4px;
        font-family: 'Georgia', serif;
    }
</style>
""", unsafe_allow_html=True)

# Set page config
st.set_page_config(
    page_title="Binary University Staff Portal",
    page_icon="🎓",
    layout="wide",
)

# Staff List (Original Order)
STAFF_LIST = [
    "Dato' Gilbert", "Mr Uthia Kumar Subramany", "Prof. Dr. Asif M Karim", 
    "Mrs. Gurvinder", "Mr. Muhammed Irfan A", "Ms. Rozmania", 
    "Ms Leeni", "Mr SK", "Ms Nurul Fatiha", "Mrs. Vani", "Mr Jegen"
]

# Week 1 Data
data_w1 = {
    "Dato' Gilbert": {"FB": "17th (PhD(ODL))", "LinkedIn": "17th (PhD(ODL))", "Telegram": "-", "WhatsApp Status": "17th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "17th (PhD(ODL))", "Remarks": "-"},
    "Mr Uthia Kumar Subramany": {"FB": "-", "LinkedIn": "17th (PhD(ODL))", "Telegram": "-", "WhatsApp Status": "17th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Prof. Dr. Asif M Karim": {"FB": "17th (PhD)", "LinkedIn": "17th, 18th (Exec MBA, PhD, Prem MBA, Prem MSc ITM)", "Telegram": "18th (PhD)", "WhatsApp Status": "17th, 18th (Exec MBA, PhD, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "17th, 18th (DBA RM, SL, PDC AI 1, 2, 3)", "Instagram": "-", "Remarks": "ResearchGate: 17th (Article)"},
    "Mrs. Gurvinder": {"FB": "-", "LinkedIn": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mr. Muhammed Irfan A": {"FB": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "LinkedIn": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Ms. Rozmania": {"FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Ms Leeni": {"FB": "17th, 18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mr SK": {"FB": "18th (PhD(ODL))", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Ms Nurul Fatiha": {"FB": "18th (Exec MBA, PhD(ODL))", "LinkedIn": "18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mrs. Vani": {"FB": "18th (Exec MBA)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mr Jegen": {"FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
}

# Week 2 Data
data_w2 = {
    "Dato' Gilbert": {"FB": "22th (PhD,25th Prem Msc)", "LinkedIn": "25th (PhD)", "Telegram": "-", "WhatsApp Status": "22th (PhD,25th Prem Msc)", "WhatsApp Group": "25th (PhD)", "Instagram": "-", "Remarks": "-"},
    "Mr Uthia Kumar Subramany": {"FB": "-", "LinkedIn": "21th Prem Msc, 23th (PhD)", "Telegram": "-", "WhatsApp Status": "21th Prem Msc, 24th Prem Msc", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Prof. Dr. Asif M Karim": {"FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "25th, 26th Prem Msc, PhD", "WhatsApp Group": "25th, 26th Prem Msc, PhD", "Instagram": "-", "Remarks": "-"},
    "Mrs. Gurvinder": {"FB": "25th Prem Msc, 25th PhD", "LinkedIn": "25th Prem Msc, 25th PhD", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mr. Muhammed Irfan A": {"FB": "25th Prem Msc, 18th, 25th PhD", "LinkedIn": "25th Prem Msc, 25th PhD", "Telegram": "25th Prem Msc", "WhatsApp Status": "23,24,25th Prem Msc, PhD", "WhatsApp Group": "-", "Instagram": "25th Prem Msc, 25th PhD", "Remarks": "-"},
    "Ms. Rozmania": {"FB": "24th Prem Msc, PhD", "LinkedIn": "24th Prem Msc, PhD", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Ms Leeni": {"FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mr SK": {"FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Ms Nurul Fatiha": {"FB": "22th Prem Msc, 22th PhD", "LinkedIn": "22th Prem Msc, 22th PhD", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mrs. Vani": {"FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "26h Prem Msc, 26h PhD", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    "Mr Jegen": {"FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
}

# Function to build df
def build_df(data_dict, week):
    rows = []
    for staff in STAFF_LIST:
        row = {"Staff Name": staff, "Week": week}
        row.update(data_dict.get(staff, {}))
        rows.append(row)
    return pd.DataFrame(rows)

df_w1 = build_df(data_w1, "Week 1")
df_w2 = build_df(data_w2, "Week 2")
df = pd.concat([df_w1, df_w2], ignore_index=True)

# Calculate post counts for graph
platform_cols = ["FB", "LinkedIn", "Telegram", "WhatsApp Status", "WhatsApp Group", "Instagram", "Remarks"]
df["Post Count"] = df[platform_cols].apply(lambda row: row.apply(lambda x: 1 if x != "-" else 0).sum(), axis=1)

# Tabs
tab1, tab2 = st.tabs(["🏠 Home", "📊 Marketing Tracker"])

with tab1:
    st.title("🎓 Welcome, Valued Staff")
    st.write("---")
    st.subheader("Why We Are Asia's Most Exclusive University")
    st.write("""
    Binary University is not a mass-market institution. We are a specialized, boutique university committed to producing 'Outstanding Talents' who command premium compensation globally.
    
    ### 🏆 The Premium Difference
    *   **Exclusive Intake:** Strict limit of **45 students** per Master’s program, DBA, and PhD ensures personalized attention.
    *   **Outcome-Oriented:** We focus on measurable professional outcomes, global mobility, and elite career preparation.
    *   **Flagship Premium MBA:** Designed to give leaders a competitive edge with a curriculum that blends leadership, innovation, and global industry requirements.

    ### ✨ Our 5 Premier USPs
    1. **ISP: Industry Specialist Professionals**
       - Description: Acquisition of deep, industry-specific skills from over 1280 Faculty of Industry Professionals transforming students into highly demanded Talents.

    2. **BEE: Binary Entrepreneurship Ecosystem thro' ACE**
       - Description: Creating Entrepreneurial Mindset Professionals with innovative problem solving and creative thinking skills nurtured through the Asia Centre for Entrepreneurship (ACE) which has over 10,500 real entrepreneurs.

    3. **WOCA: The World Is Our Campus**
       - Description: Curated study-abroad experience at another world-class university in Asia to open more career opportunities.

    4. **LII: Learning In Industry**
       - Description: True mastery happens beyond classrooms. Thro's LII, students meet leaders and shapers of industries. Real-world insights through industry visits and CEO engagements.

    5. **BTI: Guaranteed Internships with Premium Allowance**
       - Description: Guaranteed allowance of 300% higher than other universities ( RM 3000 for Masters & RM 2000 for Bachelors).

    ### 🔬 8 Centres of Research Excellence
    *   Centre for Artificial Intelligence and Data Analytics (CAIDA)
    *   Asia Centre for Entrepreneurship (ACE)
    *   Centre for Women Leadership (CWL)
    *   Centre for Advancement of Management & Leadership (CAML)
    *   Centre for Teaching and Learning (CTL)
    *   Centre for Healthcare Management (CHM)
    *   Centre for Social Entrepreneurship (CSE)
    *   ICT Centre of Excellence
    """)

with tab2:
    selected_week = st.selectbox("Select Week", ["Combined", "Week 1", "Week 2"])
    
    if selected_week != "Combined":
        display_df = df[df["Week"] == selected_week]
    else:
        display_df = df
        
    st.subheader(f"Activity Table ({selected_week})")
    st.dataframe(display_df.drop(columns=["Post Count"]), use_container_width=True)
    
    st.divider()
    st.subheader(f"Performance Overview ({selected_week})")
    # Plot using aggregated data if 'Combined', else use filtered data
    if selected_week == "Combined":
        chart_data = df.groupby("Staff Name")["Post Count"].sum().reindex(STAFF_LIST)
    else:
        chart_data = display_df.groupby("Staff Name")["Post Count"].sum().reindex(STAFF_LIST)
    st.bar_chart(chart_data)

st.divider()
st.caption("University Marketing Campaign Tracker • Streamlit")
