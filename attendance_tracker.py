import streamlit as st
import pandas as pd
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="Attendance Dashboard", layout="wide")

# --- Title ---
st.title("🎓 Student Attendance Tracker Dashboard")

# --- Sample Data or File Upload ---
st.sidebar.header("Upload CSV or Use Sample Data")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# Sample data fallback
def load_sample_data():
    return pd.DataFrame({
        "Student ID": range(1, 21),
        "Name": [f"Student {i}" for i in range(1, 21)],
        "Session": np.random.choice(["Morning", "Evening"], size=20),
        "Attendance %": np.random.randint(30, 100, size=20),
        "Last Active Date": pd.date_range(end=pd.Timestamp.today(), periods=20).strftime("%Y-%m-%d")
    })

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = load_sample_data()

# --- Filter by Session ---
session_filter = st.selectbox("🔍 Filter by Session", options=["All", "Morning", "Evening"])
if session_filter != "All":
    df = df[df["Session"] == session_filter]

# --- Summary Stats ---
st.subheader("📊 Summary Statistics")
col1, col2 = st.columns(2)
col1.metric("Total Students", len(df))
col2.metric("Average Attendance", f"{df['Attendance %'].mean():.2f}%")

# --- Top 10 Active Students ---
st.subheader("🏅 Top 10 Active Students")
top_10 = df.sort_values(by="Attendance %", ascending=False).head(10)
top_10_styled = top_10.style.apply(lambda x: ['background-color: lightgreen'] * len(x) if x.name in top_10.index else [''] * len(x), axis=1)
st.dataframe(top_10_styled, use_container_width=True)

# --- Students Below 60% ---
st.subheader("⚠️ Students Below 60% Attendance")
low_attendance = df[df["Attendance %"] < 60]
low_attendance_styled = low_attendance.style.apply(lambda x: ['background-color: #ffa8a8'] * len(x), axis=1)
st.dataframe(low_attendance_styled, use_container_width=True)

# --- All Students Table ---
st.subheader("📋 All Students")
styled_df = df.style.apply(lambda row: ['background-color: #ffa8a8' if row["Attendance %"] < 60 else '' for _ in row], axis=1)
st.dataframe(styled_df, use_container_width=True)

# --- Download CSV ---
st.subheader("⬇️ Download Filtered Data")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", data=csv, file_name="filtered_attendance.csv", mime='text/csv')

# --- Optional Visualizations ---
st.subheader("📈 Visualizations (Optional)")
chart_col1, chart_col2 = st.columns(2)

# Bar chart - Attendance Distribution
with chart_col1:
    st.markdown("**Attendance % Distribution**")
    st.bar_chart(df["Attendance %"])

# Pie chart - Session-wise count
with chart_col2:
    st.markdown("**Session-wise Student Count**")
    session_count = df["Session"].value_counts()
    st.pyplot(session_count.plot.pie(autopct="%1.1f%%", ylabel="", title="Session Distribution").figure)
