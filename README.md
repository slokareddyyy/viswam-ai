# 🎓 Student Attendance Tracker Dashboard

A clean and interactive dashboard built with **Streamlit** to help educators analyze student attendance data, highlight top performers, and identify low-attendance students in real time.

---

## 🚀 Features

- 📁 Upload your CSV or use sample data
- 🎯 Filter students by session (Morning/Evening)
- 🏅 Top 10 active students (highlighted)
- ⚠️ Flag students below 60% attendance
- 📊 Visualizations: attendance distribution, session-wise pie chart
- 📥 Export filtered data as CSV

---

## 📸 Screenshot

> *(Replace the example below with your own image)*

![Screenshot of Dashboard](assets/dashboard_example.png)

---

## 📂 Sample CSV Format

| Student ID | Name       | Session | Attendance % | Last Active Date |
|------------|------------|---------|--------------|------------------|
| 1          | John Doe   | Morning | 85           | 2024-06-01       |
| 2          | Jane Smith | Evening | 55           | 2024-06-07       |

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/attendance-dashboard.git
cd attendance-dashboard

# Install dependencies
pip install streamlit pandas numpy matplotlib

# Run the app
streamlit run attendance_dashboard.py
