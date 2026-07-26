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

# ... (data and processing remain the same)

# Data
data = [
    {"Staff Name": "Dato' Gilbert", "FB": "17th (PhD(ODL))", "LinkedIn": "17th (PhD(ODL))", "Telegram": "-", "WhatsApp Status": "17th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "17th (PhD(ODL))", "Remarks": "-"},
    {"Staff Name": "Mr Uthia Kumar Subramany", "FB": "-", "LinkedIn": "17th (PhD(ODL))", "Telegram": "-", "WhatsApp Status": "17th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Prof. Dr. Asif M Karim", "FB": "-", "LinkedIn": "17th, 18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "17th, 18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "WhatsApp Group": "17th, 18th (DBA RM, SL, PDC AI 1, 2, 3)", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mrs. Gurvinder", "FB": "-", "LinkedIn": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr. Muhammed Irfan A", "FB": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "LinkedIn": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms. Rozmania", "FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms Leeni", "FB": "17th, 18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL), Exec MBA, Prem MBA, Prem MSc ITM)", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr SK", "FB": "18th (PhD(ODL))", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "18th (PhD(ODL))", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Ms Nurul Fatiha", "FB": "18th (Exec MBA, PhD(ODL))", "LinkedIn": "18th (Exec MBA, PhD(ODL), Prem MBA, Prem MSc ITM)", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mrs. Vani", "FB": "18th (Exec MBA)", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
    {"Staff Name": "Mr Jegen", "FB": "-", "LinkedIn": "-", "Telegram": "-", "WhatsApp Status": "-", "WhatsApp Group": "-", "Instagram": "-", "Remarks": "-"},
]

df = pd.DataFrame(data)

# Calculate post counts for graph
platform_cols = ["FB", "LinkedIn", "Telegram", "WhatsApp Status", "WhatsApp Group", "Instagram"]
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
    1. **Industry-Relevant Curriculum:** Constantly updated to meet global market demands.
    2. **Entrepreneurship Focus:** Entrepreneurial skills are embedded into our postgraduate DNA.
    3. **Global Alumni Network:** Access to industry leaders worldwide.
    4. **Research-Driven:** Deep academic insight through our specialized centres.
    5. **Exclusive Environment:** Small class sizes foster high-level networking.

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
    st.subheader("Week 1 Activity Table (July 17-18)")
    st.dataframe(df.drop(columns=["Post Count"]), use_container_width=True)
    
    st.divider()
    st.subheader("Performance Overview")
    chart_data = df[["Staff Name", "Post Count"]].set_index("Staff Name")
    st.bar_chart(chart_data)

st.divider()
st.caption("University Marketing Campaign Tracker • Streamlit")
