import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as px

from scipy import stats

st.set_page_config(
    page_title="Aplikasi Statistik",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Aplikasi Analisis Data Statistik")
st.write("Upload file CSV untuk melakukan analisis statistik.")

uploaded_file = st.file_uploader(
    "Upload File CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")

    st.dataframe(df)

    st.write("Jumlah Data :", df.shape[0])
    st.write("Jumlah Variabel :", df.shape[1])

    numeric = df.select_dtypes(include=np.number)

    st.subheader("Statistik Deskriptif")

    st.dataframe(numeric.describe())

    st.subheader("Missing Value")

    st.write(df.isnull().sum())

    st.subheader("Pilih Variabel")

    kolom = st.selectbox(
        "Kolom",
        numeric.columns
    )

    st.subheader("Histogram")

    fig = px.histogram(
        df,
        x=kolom,
        nbins=20
    )

    st.plotly_chart(fig)

    st.subheader("Boxplot")

    fig2 = px.box(
        df,
        y=kolom
    )

    st.plotly_chart(fig2)

    st.subheader("Mean")

    st.success(numeric[kolom].mean())

    st.subheader("Median")

    st.success(numeric[kolom].median())

    st.subheader("Modus")

    st.success(numeric[kolom].mode()[0])

    st.subheader("Standar Deviasi")

    st.success(numeric[kolom].std())

    st.subheader("Varians")

    st.success(numeric[kolom].var())

    st.subheader("Minimum")

    st.success(numeric[kolom].min())

    st.subheader("Maximum")

    st.success(numeric[kolom].max())

    st.subheader("Uji Normalitas (Shapiro-Wilk)")

    statistic, p = stats.shapiro(
        numeric[kolom]
    )

    st.write("Statistik :", statistic)
    st.write("P-Value :", p)

    if p > 0.05:
        st.success("Data berdistribusi normal")
    else:
        st.error("Data tidak normal")

    st.subheader("Korelasi")

    corr = numeric.corr()

    fig3 = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r"
    )

    st.plotly_chart(fig3)

    st.subheader("Scatter Plot")

    x = st.selectbox(
        "Sumbu X",
        numeric.columns,
        key=1
    )

    y = st.selectbox(
        "Sumbu Y",
        numeric.columns,
        key=2
    )

    fig4 = px.scatter(
        df,
        x=x,
        y=y,
        trendline="ols"
    )

    st.plotly_chart(fig4)

else:

    st.info("Silakan upload file CSV.")
