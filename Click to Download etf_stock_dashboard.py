
import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("ETF_Stock_Analyzer.xlsx", sheet_name=None)

data = load_data()

# Sidebar Filters
st.sidebar.title("Filters")
selected_type = st.sidebar.multiselect("Select Type", options=["ETF", "STK"], default=["ETF", "STK"])
selected_sector = st.sidebar.multiselect("Select Sector", options=data['Full Dataset']['Sector'].unique())

# Dashboard Tabs
st.title("📊 ETF & Stock Analyzer Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(["Full Dataset", "Top Performers", "Forecast Leaders", "401(k) Comparison"])

with tab1:
    st.subheader("🔍 Full Dataset")
    df = data['Full Dataset']
    if selected_type:
        df = df[df['Type'].isin(selected_type)]
    if selected_sector:
        df = df[df['Sector'].isin(selected_sector)]
    st.dataframe(df)

with tab2:
    st.subheader("🏆 Top Performers by 10Y CAGR")
    df = data['Full Dataset']
    df = df[df['Type'].isin(selected_type)]
    df = df.sort_values('10Y CAGR', ascending=False).head(50)
    st.dataframe(df)

with tab3:
    st.subheader("🔮 Forecast Leaders")
    df = data['Forecast Leaders']
    df = df[df['Type'].isin(selected_type)]
    df = df.sort_values('Forecasted 1Y Return', ascending=False).head(50)
    st.dataframe(df)

with tab4:
    st.subheader("💼 401(k) Comparison")
    st.write("This section will highlight your holdings when integrated. Coming soon!")
