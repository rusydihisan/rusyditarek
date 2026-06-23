import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Dashboard Rusydi",
    page_icon="📊",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    return pd.read_csv("Mall_Customers.csv")

df = load_data()

# Ganti nama kolom
df.columns = [
    "Customer ID",
    "Gender",
    "Age",
    "Annual Income",
    "Spending Score"
]

# =========================
# HEADER
# =========================
st.markdown("""
<h1 style='text-align:center; color:#1E88E5;'>
📊 Dashboard Analisis Pelanggan Mall
</h1>
<h3 style='text-align:center;'>
Muhammad Rusydi Hisan
</h3>
<hr>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("Menu Dashboard")

gender = st.sidebar.selectbox(
    "Filter Gender",
    ["Semua", "Male", "Female"]
)

if gender != "Semua":
    df = df[df["Gender"] == gender]

# =========================
# KPI
# =========================
st.subheader("Ringkasan Data")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Jumlah Pelanggan", len(df))

with col2:
    st.metric("Rata-rata Umur", round(df["Age"].mean(), 1))

with col3:
    st.metric("Income Rata-rata", round(df["Annual Income"].mean(), 1))

with col4:
    st.metric("Spending Rata-rata", round(df["Spending Score"].mean(), 1))

st.divider()

# =========================
# GRAFIK
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribusi Gender")

    gender_count = df["Gender"].value_counts()

    fig, ax = plt.subplots()
    ax.pie(
        gender_count,
        labels=gender_count.index,
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

with col2:
    st.subheader("Distribusi Umur")

    fig, ax = plt.subplots()
    ax.hist(df["Age"], bins=10)

    ax.set_xlabel("Umur")
    ax.set_ylabel("Jumlah Pelanggan")

    st.pyplot(fig)

# =========================
# SCATTER PLOT
# =========================
st.subheader("Hubungan Income dan Spending Score")

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(
    df["Annual Income"],
    df["Spending Score"]
)

ax.set_xlabel("Annual Income")
ax.set_ylabel("Spending Score")
ax.set_title("Income vs Spending Score")

st.pyplot(fig)

# =========================
# DATASET
# =========================
st.subheader("Data Pelanggan")

st.dataframe(
    df,
    use_container_width=True
)

# =========================
# FOOTER
# =========================
st.markdown("""
<hr>
<p style='text-align:center;'>
© 2026 | Dashboard Analisis Pelanggan Mall
<br>
Dibuat oleh Muhammad Rusydi Hisan
</p>
""", unsafe_allow_html=True)
