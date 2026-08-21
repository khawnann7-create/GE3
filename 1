import streamlit as st
import pandas as pd
import plotly.express as px
# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
   page_title="Smart Bin Alert",
   page_icon="🗑️",
   layout="wide"
)
st.title("🗑️ Smart Bin Alert Dashboard")
st.markdown("ระบบแจ้งเตือนสถานะถังขยะภายในหอพัก")
# ---------------------------
# Sample Data
# ---------------------------
data = {
   "ถังขยะ": ["A", "B", "C", "D", "E"],
   "สถานที่": [
       "หอชาย ชั้น 1",
       "หอชาย ชั้น 3",
       "หอหญิง ชั้น 1",
       "หอหญิง ชั้น 2",
       "โรงอาหาร"
   ],
   "ระดับขยะ (%)": [20, 75, 95, 40, 85]
}
df = pd.DataFrame(data)
# ---------------------------
# Status Function
# ---------------------------
def get_status(level):
   if level >= 90:
       return "เต็ม"
   elif level >= 70:
       return "ใกล้เต็ม"
   else:
       return "ว่าง"
df["สถานะ"] = df["ระดับขยะ (%)"].apply(get_status)
# ---------------------------
# KPI Cards
# ---------------------------
total_bins = len(df)
full_bins = len(df[df["สถานะ"] == "เต็ม"])
warning_bins = len(df[df["สถานะ"] == "ใกล้เต็ม"])
col1, col2, col3 = st.columns(3)
col1.metric("จำนวนถังทั้งหมด", total_bins)
col2.metric("ถังขยะเต็ม", full_bins)
col3.metric("ถังขยะใกล้เต็ม", warning_bins)
st.divider()
# ---------------------------
# Table
# ---------------------------
st.subheader("📋 สถานะถังขยะ")
st.dataframe(
   df,
   use_container_width=True
)
# ---------------------------
# Alert Section
# ---------------------------
st.subheader("🚨 การแจ้งเตือน")
for _, row in df.iterrows():
   if row["สถานะ"] == "เต็ม":
       st.error(
           f"ถังขยะ {row['ถังขยะ']} ({row['สถานที่']}) เต็มแล้ว กรุณาเข้าดำเนินการ"
       )
   elif row["สถานะ"] == "ใกล้เต็ม":
       st.warning(
           f"ถังขยะ {row['ถังขยะ']} ({row['สถานที่']}) ใกล้เต็ม"
       )
# ---------------------------
# Bar Chart
# ---------------------------
st.subheader("📊 ระดับขยะแต่ละจุด")
fig_bar = px.bar(
   df,
   x="ถังขยะ",
   y="ระดับขยะ (%)",
   color="สถานะ",
   text="ระดับขยะ (%)"
)
st.plotly_chart(fig_bar, use_container_width=True)
# ---------------------------
# Pie Chart
# ---------------------------
st.subheader("🥧 สัดส่วนสถานะถังขยะ")
status_count = (
   df["สถานะ"]
   .value_counts()
   .reset_index()
)
status_count.columns = ["สถานะ", "จำนวน"]
fig_pie = px.pie(
   status_count,
   names="สถานะ",
   values="จำนวน",
   hole=0.4
)
st.plotly_chart(fig_pie, use_container_width=True)
# ---------------------------
# Historical Data Example
# ---------------------------
st.subheader("📈 สถิติการเก็บขยะรายสัปดาห์")
history = pd.DataFrame({
   "วัน": ["จันทร์","อังคาร","พุธ","พฤหัส","ศุกร์","เสาร์","อาทิตย์"],
   "จำนวนการแจ้งเตือน": [3,5,2,6,4,7,3]
})
fig_line = px.line(
   history,
   x="วัน",
   y="จำนวนการแจ้งเตือน",
   markers=True
)
st.plotly_chart(fig_line, use_container_width=True)
st.success("ระบบพร้อมเชื่อมต่อข้อมูลจากเซ็นเซอร์ IoT ในอนาคต")
