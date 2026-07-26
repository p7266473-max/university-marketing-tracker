import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="University Staff Portal",
    page_icon="🎓",
    layout="wide",
)

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
    st.subheader("Your Impact Matters")
    st.write("""
    Thank you for your dedication to Binary University. As representatives of Asia's Most Exclusive University, 
    your efforts in sharing our vision of producing 'Outstanding Talents' are invaluable. 
    
    **Remember to emphasize:**
    *   **Elite Education:** Specialized DBA, PhD, MBA, and MSc programs.
    *   **Measurable Outcomes:** We focus on career readiness and premium industry placement.
    *   **Research Excellence:** Our 8 Research Centres of Excellence drive innovation.
    
    You are key to our mission of nurturing industry leaders. Keep up the great work!
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
