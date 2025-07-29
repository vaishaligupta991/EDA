import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="EDA Dashboard", layout="wide")
st.title("📊 Exploratory Data Analysis (EDA)")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Dataset Overview")
    st.write(df.head())
    st.markdown("**Shape of dataset:**")
    st.write(f"{df.shape[0]} rows and {df.shape[1]} columns")
    st.markdown("**Column Data Types:**")
    st.write(df.dtypes)
    st.markdown("**Missing Values:**")
    st.write(df.isnull().sum())
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())
    st.subheader("📌 Correlation Heatmap")
    if df.select_dtypes(include=["float64", "int64"]).shape[1] >= 2:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)
    else:
        st.write("Not enough numeric columns to show correlation.")
    st.subheader("📊 Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        col = st.selectbox("Select Column for Distribution Plot", df.select_dtypes(include=["float64", "int64"]).columns)
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, bins=30, ax=ax)
        st.pyplot(fig)
    with col2:
        num_col = st.selectbox("Select Numeric Column for Boxplot", df.select_dtypes(include=["float64", "int64"]).columns)
        fig, ax = plt.subplots()
        sns.boxplot(x=df[num_col], ax=ax)
        st.pyplot(fig)
    st.subheader("🧮 Value Counts for Categorical Columns")
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    for col in cat_cols:
        st.markdown(f"**{col}**")
        st.write(df[col].value_counts())
else:
    st.info("👈 Upload a CSV file to begin EDA.")
