import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Mall Customer Dashboard",
    layout="wide"
)

# Cache data agar tidak dibaca berulang
@st.cache_data
def load_data():
    return pd.read_csv("Mall_Customers.csv")

df = load_data()

# Rename kolom
df.columns = [
    "CustomerID",
    "Gender",
    "Age",
    "Annual Income",
    "Spending Score"
]

# Header
st.title("📊 Mall Customer Dashboard")
st.write("Analisis Data Pelanggan Mall")

# KPI
col1, col2, col3 = st.columns(3)

col1.metric("Jumlah Pelanggan", len(df))
col2.metric("Rata-rata Umur", round(df["Age"].mean(), 1))
col3.metric("Rata-rata Spending", round(df["Spending Score"].mean(), 1))

st.divider()

# Grafik
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
    ax.set_xlabel("Age")
    ax.set_ylabel("Jumlah")
    st.pyplot(fig)

st.divider()

# Scatter sederhana
st.subheader("Income vs Spending Score")

fig, ax = plt.subplots(figsize=(8,5))

ax.scatter(
    df["Annual Income"],
    df["Spending Score"]
)

ax.set_xlabel("Annual Income")
ax.set_ylabel("Spending Score")

st.pyplot(fig)

st.divider()

# Dataset
st.subheader("Dataset")

st.dataframe(
    df,
    use_container_width=True
)
