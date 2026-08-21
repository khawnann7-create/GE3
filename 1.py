# ==========================================
# Smart Bin Alert Dashboard
# ระบบแจ้งเตือนสถานะถังขยะอัจฉริยะในหอพัก
# Developed with Streamlit
# ==========================================
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# ------------------------------------------
# PAGE CONFIG
# ------------------------------------------
st.set_page_config(
   page_title="Smart Bin Alert",
   page_icon="🗑️",
   layout="wide"
)
# ------------------------------------------
# CUSTOM CSS
# ------------------------------------------
st.markdown("""
<style>
.main {
   background-color: #F8FAFC;
}
.title {
   text-align:center;
   font-size:45px;
   font-weight:bold;
   color:#2563EB;
}
.subtitle {
   text-align:center;
   font-size:20px;
   color:#64748B;
   margin-bottom:20px;
}
.kpi-card {
   padding:20px;
   border-radius:20px;
   text-align:center;
   color:white;
   font-weight:bold;
}
.full-card{
   background:linear-gradient(135deg,#FF416C,#FF4B2B);
}
.warning-card{
   background:linear-gradient(135deg,#F7971E,#FFD200);
}
.normal-card{
   background:linear-gradient(135deg,#00C9A7,#00E4A0);
}
.big-font{
   font-size:35px;
}
</style>
""", unsafe_allow_html=True)
# ------------------------------------------
# HEADER
# ------------------------------------------
st.markdown(
   '<p class="title">🗑️ Smart Bin Alert Dashboard</p>',
   unsafe_allow_html=True
)
st.markdown(
   '<p class="subtitle">ระบบแจ้งเตือนสถานะถังขยะอัจฉริยะภายในหอพักนักศึกษา</p>',
   unsafe_allow_html=True
)
# ------------------------------------------
# SIDEBAR
# ------------------------------------------
st.sidebar.image(
   "https://cdn-icons-png.flaticon.com/512/3082/3082037.png",
   width=120
)
st.sidebar.title("⚙️ เมนูควบคุม")
selected_building = st.sidebar.selectbox(
   "เลือกอาคาร",
   ["ทั้งหมด", "หอชาย", "หอหญิง", "โรงอาหาร"]
)
refresh = st.sidebar.button("🔄 รีเฟรชข้อมูล")
# ------------------------------------------
# SAMPLE DATA
# ------------------------------------------
data = {
   "ถังขยะ": ["A01","A02","A03","B01","B02","C01","C02"],
   "อาคาร": [
       "หอชาย",
       "หอชาย",
       "หอชาย",
       "หอหญิง",
       "หอหญิง",
       "โรงอาหาร",
       "โรงอาหาร"
   ],
   "ตำแหน่ง": [
       "ชั้น 1",
       "ชั้น 2",
       "ชั้น 3",
       "ชั้น 1",
       "ชั้น 2",
       "หน้าโรงอาหาร",
       "หลังโรงอาหาร"
   ],
   "ระดับขยะ": [25, 78, 95, 40, 88, 99, 60]
}
df = pd.DataFrame(data)
# ------------------------------------------
# STATUS FUNCTION
# ------------------------------------------
def get_status(level):
   if level >= 90:
       return "เต็ม"
   elif level >= 70:
       return "ใกล้เต็ม"
   else:
       return "ว่าง"
df["สถานะ"] = df["ระดับขยะ"].apply(get_status)
# ------------------------------------------
# FILTER
# ------------------------------------------
if selected_building != "ทั้งหมด":
   df = df[df["อาคาร"] == selected_building]
# ------------------------------------------
# KPI
# ------------------------------------------
total_bins = len(df)
full_bins = len(df[df["สถานะ"]=="เต็ม"])
warning_bins = len(df[df["สถานะ"]=="ใกล้เต็ม"])
col1,col2,col3 = st.columns(3)
with col1:
   st.markdown(f"""
<div class="kpi-card normal-card">
<h3>🗑️ ถังทั้งหมด</h3>
<div class="big-font">{total_bins}</div>
</div>
   """, unsafe_allow_html=True)
with col2:
   st.markdown(f"""
<div class="kpi-card warning-card">
<h3>⚠️ ใกล้เต็ม</h3>
<div class="big-font">{warning_bins}</div>
</div>
   """, unsafe_allow_html=True)
with col3:
   st.markdown(f"""
<div class="kpi-card full-card">
<h3>🚨 เต็ม</h3>
<div class="big-font">{full_bins}</div>
</div>
   """, unsafe_allow_html=True)
st.write("")
st.divider()
# ------------------------------------------
# ALERT SECTION
# ------------------------------------------
st.subheader("🚨 การแจ้งเตือนล่าสุด")
for _, row in df.iterrows():
   if row["สถานะ"] == "เต็ม":
       st.error(
           f"ถัง {row['ถังขยะ']} ({row['อาคาร']} {row['ตำแหน่ง']}) เต็มแล้ว กรุณาเข้าจัดเก็บ"
       )
   elif row["สถานะ"] == "ใกล้เต็ม":
       st.warning(
           f"ถัง {row['ถังขยะ']} ({row['อาคาร']} {row['ตำแหน่ง']}) ใกล้เต็ม"
       )
# ------------------------------------------
# DATA TABLE
# ------------------------------------------
st.subheader("📋 ตารางสถานะถังขยะ")
st.dataframe(
   df,
   use_container_width=True,
   hide_index=True
)
# ------------------------------------------
# CHART SECTION
# ------------------------------------------
col_chart1,col_chart2 = st.columns(2)
# BAR CHART
with col_chart1:
   st.subheader("📊 ระดับขยะของแต่ละถัง")
   fig_bar = px.bar(
       df,
       x="ถังขยะ",
       y="ระดับขยะ",
       color="สถานะ",
       text="ระดับขยะ",
       color_discrete_map={
           "เต็ม":"red",
           "ใกล้เต็ม":"orange",
           "ว่าง":"green"
       }
   )
   fig_bar.update_layout(
       height=450,
       template="plotly_white"
   )
   st.plotly_chart(
       fig_bar,
       use_container_width=True
   )
# PIE CHART
with col_chart2:
   st.subheader("🥧 สัดส่วนสถานะถังขยะ")
   status_count = (
       df["สถานะ"]
       .value_counts()
       .reset_index()
   )
   status_count.columns = [
       "สถานะ",
       "จำนวน"
   ]
   fig_pie = px.pie(
       status_count,
       names="สถานะ",
       values="จำนวน",
       hole=0.5
   )
   fig_pie.update_layout(
       height=450
   )
   st.plotly_chart(
       fig_pie,
       use_container_width=True
   )
# ------------------------------------------
# WEEKLY TREND
# ------------------------------------------
st.subheader("📈 แนวโน้มการแจ้งเตือนรายสัปดาห์")
weekly = pd.DataFrame({
   "วัน":[
       "จันทร์",
       "อังคาร",
       "พุธ",
       "พฤหัสบดี",
       "ศุกร์",
       "เสาร์",
       "อาทิตย์"
   ],
   "จำนวนแจ้งเตือน":[
       3,
       5,
       2,
       7,
       6,
       8,
       4
   ]
})
fig_line = px.line(
   weekly,
   x="วัน",
   y="จำนวนแจ้งเตือน",
   markers=True
)
fig_line.update_traces(
   line_width=5
)
fig_line.update_layout(
   height=500,
   template="plotly_white"
)
st.plotly_chart(
   fig_line,
   use_container_width=True
)
# ------------------------------------------
# PROGRESS BARS
# ------------------------------------------
st.subheader("📍 ระดับขยะแบบ Real-Time")
for _, row in df.iterrows():
   st.write(
       f"🗑️ ถัง {row['ถังขยะ']} | {row['อาคาร']} | {row['ตำแหน่ง']}"
   )
   st.progress(
       int(row["ระดับขยะ"])
   )
   st.write(
       f"ระดับขยะ {row['ระดับขยะ']}%"
   )
# ------------------------------------------
# FOOTER
# ------------------------------------------
st.divider()
st.success(
   "✅ ระบบต้นแบบพร้อมต่อยอดเชื่อมต่อ IoT Sensor (ESP32 + Ultrasonic Sensor)"
)
st.info(
   "📡 สามารถเพิ่มการแจ้งเตือนผ่าน LINE, Email และ Mobile App ได้ในอนาคต"
)
