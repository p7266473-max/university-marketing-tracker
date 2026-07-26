import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="University Marketing Campaign Tracker - Week 1",
    page_icon="🎓",
    layout="wide",
)

st.title("🎓 University Staff Marketing Campaign Tracker (Week 1: July 17-18)")
st.markdown("**Weekly social media tracking for staff.**")
st.divider()

# Data provided by user
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

st.subheader("Week 1 Activity Table")
st.dataframe(df, use_container_width=True)

st.divider()
st.caption("University Marketing Campaign Tracker • Streamlit")
