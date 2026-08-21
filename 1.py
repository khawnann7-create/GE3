import streamlit as st

import pandas as pd

# =========================

# ตั้งค่าหน้าเว็บ

# =========================

st.set_page_config(

    page_title="Smart Bin Alert",

    page_icon="🗑️",

    layout="wide"

)

# =========================

# CSS

# =========================

st.markdown("""
<style>

.main{

    background-color:#F5F7FA;

}

.title{

    text-align:center;

    font-size:42px;

    font-weight:bold;

    color:#0F62FE;

}

.card{

    padding:20px;

    border-radius:15px;

    text-align:center;

    color:white;

    font-weight:bold;

}

.green{

    background:#22C55E;

}

.orange{

    background:#F59E0B;

}

.red{

    background:#EF4444;

}
</style>

""", unsafe_allow_html=True)

# =========================

# Header

# =========================

st.markdown(

    '<p class="title">🗑️ Smart Bin Alert Dashboard</p>',

    unsafe_allow_html=True

)

st.write("### ระบบแจ้งเตือนสถานะถังขยะอัจฉริยะ")

# =========================

# ข้อมูลตัวอย่าง

# =========================

data = {

    "ถังขยะ":["A01","A02","B01","B02","C01"],

    "ตำแหน่ง":[

        "ลานดาว",

        "สวนแฟนฉัน",

        "ทางเดินโรงอาหาร",

        "หน้าหอพัก หญิง",

        "หน้าหอพักชาย"

    ],

    "ระดับขยะ":[25,75,95,60,88]

}

df = pd.DataFrame(data)

# =========================

# สถานะ

# =========================

def status(level):

    if level >= 90:

        return "เต็ม"

    elif level >= 70:

        return "ใกล้เต็ม"

    else:

        return "ว่าง"

df["สถานะ"] = df["ระดับขยะ"].apply(status)

# =========================

# KPI

# =========================

total = len(df)

full = len(df[df["สถานะ"]=="เต็ม"])

warning = len(df[df["สถานะ"]=="ใกล้เต็ม"])

c1,c2,c3 = st.columns(3)

with c1:

    st.metric("🗑️ ถังทั้งหมด", total)

with c2:

    st.metric("⚠️ ใกล้เต็ม", warning)

with c3:

    st.metric("🚨 เต็ม", full)

st.divider()

# =========================

# แจ้งเตือน

# =========================

st.subheader("🚨 การแจ้งเตือน")

for _, row in df.iterrows():

    if row["สถานะ"] == "เต็ม":

        st.error(

            f"ถัง {row['ถังขยะ']} ({row['ตำแหน่ง']}) เต็มแล้ว"

        )

    elif row["สถานะ"] == "ใกล้เต็ม":

        st.warning(

            f"ถัง {row['ถังขยะ']} ({row['ตำแหน่ง']}) ใกล้เต็ม"

        )

# =========================

# ตาราง

# =========================

st.subheader("📋 สถานะถังขยะ")

st.dataframe(

    df,

    use_container_width=True

)

# =========================

# Progress Bar

# =========================

st.subheader("📊 ระดับขยะแต่ละถัง")

for _, row in df.iterrows():

    st.write(

        f"🗑️ {row['ถังขยะ']} - {row['ตำแหน่ง']}"

    )

    st.progress(

        int(row["ระดับขยะ"])

    )

    st.write(

        f"{row['ระดับขยะ']}%"

    )

# =========================



st.success(

    "ระบบพร้อมใช้งานและสามารถต่อยอดเชื่อมต่อ IoT Sensor ได้"

)
 
